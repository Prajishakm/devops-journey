# Lab 03 – API → SQLite

**Goal:** Combine Python + your SQL knowledge: fetch JSON from a REST API and store it in a database.

## Task
Fill in the `TODO`s in `weather_to_sql.py`. Tests use a fake API, so they work offline.

```bash
pytest -v
python weather_to_sql.py      # real call → creates weather.db
sqlite3 weather.db "SELECT * FROM readings LIMIT 5;"
```

## Stretch goals
- Add a `city` column and store Helsinki + Tampere + Oulu
- Schedule it hourly with `cron` (`crontab -e`) – your Linux skills!
- Handle network errors gracefully (try/except `requests.RequestException`)
