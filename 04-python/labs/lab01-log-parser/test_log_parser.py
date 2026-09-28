from pathlib import Path

from log_parser import error_rate, parse_file, parse_line, status_counts, top_ips

SAMPLE = Path(__file__).parent / "sample_access.log"


def test_parse_valid_line():
    line = '10.0.0.5 - - [28/Sep/2026:10:02:30 +0300] "GET /admin HTTP/1.1" 403 256'
    e = parse_line(line)
    assert e["ip"] == "10.0.0.5"
    assert e["method"] == "GET"
    assert e["path"] == "/admin"
    assert e["status"] == 403
    assert e["size"] == 256


def test_parse_bad_line_returns_none():
    assert parse_line("garbage") is None


def test_parse_file_skips_bad_lines():
    assert len(parse_file(SAMPLE)) == 8


def test_top_ips():
    assert top_ips(parse_file(SAMPLE), 1) == [("192.168.1.10", 3)]


def test_status_counts():
    counts = status_counts(parse_file(SAMPLE))
    assert counts[200] == 4
    assert counts[404] == 1


def test_error_rate():
    assert error_rate(parse_file(SAMPLE)) == 50.0


def test_error_rate_empty():
    assert error_rate([]) == 0.0
