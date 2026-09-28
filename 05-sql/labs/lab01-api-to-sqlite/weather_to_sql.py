"""Lab 03 – Pull data from a REST API and store it in SQLite.

API: Open-Meteo (free, no API key) – hourly temperature for Helsinki.
Run:  python weather_to_sql.py
Test: pytest -v
"""
import sqlite3

import requests

API_URL = "https://api.open-meteo.com/v1/forecast"
HELSINKI = {"latitude": 60.17, "longitude": 24.94}


def fetch_weather(latitude, longitude):
    """Call the API and return the JSON as a dict.
    Params: latitude, longitude, hourly="temperature_2m", forecast_days=1"""
    # TODO: requests.get(API_URL, params=..., timeout=10)
    #       call .raise_for_status() and return .json()
    raise NotImplementedError


def to_rows(data):
    """Turn API JSON into a list of (time, temperature) tuples.
    data["hourly"]["time"] and data["hourly"]["temperature_2m"] are parallel lists."""
    # TODO: hint – zip()
    raise NotImplementedError


def init_db(conn):
    """Create table readings(time TEXT PRIMARY KEY, temperature REAL) if missing."""
    # TODO: conn.execute("CREATE TABLE IF NOT EXISTS ...")
    raise NotImplementedError


def save_rows(conn, rows):
    """Insert rows; re-running must NOT create duplicates. Return number of rows in table."""
    # TODO: INSERT OR REPLACE ... with conn.executemany, then conn.commit()
    #       then SELECT COUNT(*) FROM readings
    raise NotImplementedError


def stats(conn):
    """Return (min, max, avg rounded to 1 decimal) temperature using ONE SQL query."""
    # TODO: SELECT MIN(...), MAX(...), AVG(...) FROM readings
    raise NotImplementedError


if __name__ == "__main__":
    data = fetch_weather(**HELSINKI)
    conn = sqlite3.connect("weather.db")
    init_db(conn)
    total = save_rows(conn, to_rows(data))
    lo, hi, avg = stats(conn)
    print(f"Rows in DB: {total}")
    print(f"Helsinki today → min {lo}°C, max {hi}°C, avg {avg}°C")
