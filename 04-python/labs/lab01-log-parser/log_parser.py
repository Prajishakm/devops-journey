"""Lab 02 – Parse web server (Apache/Nginx) access logs.

Run:  python log_parser.py sample_access.log
Test: pytest -v
"""
import re
import sys
from collections import Counter

# One log line looks like:
# 192.168.1.10 - - [28/Sep/2026:10:00:01 +0300] "GET /index.html HTTP/1.1" 200 5120
LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d{3}) (?P<size>\d+)'
)


def parse_line(line):
    """Return a dict with ip, time, method, path, status (int), size (int).
    Return None if the line doesn't match."""
    # TODO: use LOG_PATTERN.match(line); convert status and size to int
    raise NotImplementedError


def parse_file(path):
    """Return a list of parsed dicts, skipping bad lines."""
    # TODO: open the file, call parse_line on each line, keep non-None results
    raise NotImplementedError


def top_ips(entries, n=3):
    """Return the n most common IPs as [(ip, count), ...]."""
    # TODO: hint – collections.Counter(...).most_common(n)
    raise NotImplementedError


def status_counts(entries):
    """Return {status_code: count}."""
    # TODO
    raise NotImplementedError


def error_rate(entries):
    """Percentage (0-100, rounded to 1 decimal) of requests with status >= 400."""
    # TODO: watch out for an empty list!
    raise NotImplementedError


if __name__ == "__main__":
    logfile = sys.argv[1] if len(sys.argv) > 1 else "sample_access.log"
    entries = parse_file(logfile)
    print(f"Total requests: {len(entries)}")
    print(f"Top IPs: {top_ips(entries)}")
    print(f"Status codes: {status_counts(entries)}")
    print(f"Error rate: {error_rate(entries)}%")
