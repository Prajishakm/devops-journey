import sqlite3

import pytest

import sysmon


@pytest.fixture
def conn():
    c = sqlite3.connect(":memory:")
    sysmon.init_db(c)
    yield c
    c.close()


def test_collect_returns_percentages():
    s = sysmon.collect()
    assert set(s) == {"time", "cpu", "memory", "disk"}
    for key in ("cpu", "memory", "disk"):
        assert 0 <= s[key] <= 100


def test_no_alerts_when_healthy():
    s = {"time": "t", "cpu": 10, "memory": 20, "disk": 30}
    assert sysmon.check_alerts(s) == []


def test_alert_when_disk_high():
    s = {"time": "t", "cpu": 10, "memory": 20, "disk": 95.0}
    alerts = sysmon.check_alerts(s)
    assert len(alerts) == 1
    assert alerts[0].startswith("disk")


def test_save_and_latest_order(conn):
    for i in range(3):
        sysmon.save(conn, {"time": f"t{i}", "cpu": i, "memory": i, "disk": i})
    rows = sysmon.latest(conn, 2)
    assert [r["time"] for r in rows] == ["t2", "t1"]
