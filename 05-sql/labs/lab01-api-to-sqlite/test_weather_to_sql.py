import sqlite3

import pytest

import weather_to_sql as w

FAKE = {
    "hourly": {
        "time": ["2026-09-28T00:00", "2026-09-28T01:00", "2026-09-28T02:00"],
        "temperature_2m": [8.0, 10.0, 12.5],
    }
}


class FakeResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return FAKE


@pytest.fixture
def conn():
    c = sqlite3.connect(":memory:")
    w.init_db(c)
    yield c
    c.close()


def test_fetch_uses_params(monkeypatch):
    seen = {}

    def fake_get(url, params=None, timeout=None):
        seen.update(params)
        return FakeResponse()

    monkeypatch.setattr(w.requests, "get", fake_get)
    assert w.fetch_weather(60.17, 24.94) == FAKE
    assert seen["latitude"] == 60.17
    assert seen["hourly"] == "temperature_2m"


def test_to_rows():
    assert w.to_rows(FAKE)[0] == ("2026-09-28T00:00", 8.0)
    assert len(w.to_rows(FAKE)) == 3


def test_save_is_idempotent(conn):
    rows = w.to_rows(FAKE)
    assert w.save_rows(conn, rows) == 3
    assert w.save_rows(conn, rows) == 3  # no duplicates


def test_stats(conn):
    w.save_rows(conn, w.to_rows(FAKE))
    assert w.stats(conn) == (8.0, 12.5, 10.2)
