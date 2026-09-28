"""sysmon v1 – collect CPU / memory / disk metrics and store them in SQLite.

This project grows every phase (Docker → Kubernetes → Azure → Terraform → Grafana).

Usage:
  python sysmon.py collect            # take one sample
  python sysmon.py collect --every 5  # sample every 5 seconds (Ctrl+C to stop)
  python sysmon.py report             # show last 10 samples + alerts
"""
import argparse
import sqlite3
import time
from datetime import datetime

import psutil

DB_PATH = "sysmon.db"
THRESHOLDS = {"cpu": 90.0, "memory": 85.0, "disk": 80.0}


def collect():
    """Return {"time": ISO string, "cpu": %, "memory": %, "disk": %} for this machine."""
    # TODO: psutil.cpu_percent(interval=1), psutil.virtual_memory().percent,
    #       psutil.disk_usage("/").percent, datetime.now().isoformat(timespec="seconds")
    raise NotImplementedError


def check_alerts(sample, thresholds=THRESHOLDS):
    """Return a list like ["cpu 95.0% > 90.0%"] for every metric above its threshold."""
    # TODO
    raise NotImplementedError


def init_db(conn):
    """Create table metrics(id INTEGER PRIMARY KEY AUTOINCREMENT, time TEXT,
    cpu REAL, memory REAL, disk REAL)."""
    # TODO
    raise NotImplementedError


def save(conn, sample):
    """Insert one sample."""
    # TODO: use ? placeholders, never f-strings in SQL!
    raise NotImplementedError


def latest(conn, n=10):
    """Return the n newest samples as a list of dicts, newest first."""
    # TODO: ORDER BY id DESC LIMIT ?
    raise NotImplementedError


def main():
    parser = argparse.ArgumentParser(description="Tiny system monitor")
    sub = parser.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("collect")
    c.add_argument("--every", type=int, help="seconds between samples")
    sub.add_parser("report")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    init_db(conn)

    if args.cmd == "collect":
        while True:
            s = collect()
            save(conn, s)
            print(s, *check_alerts(s), sep="  ")
            if not args.every:
                break
            time.sleep(args.every)
    else:
        for s in latest(conn):
            print(f'{s["time"]}  cpu {s["cpu"]:5.1f}%  mem {s["memory"]:5.1f}%  disk {s["disk"]:5.1f}%')


if __name__ == "__main__":
    main()
