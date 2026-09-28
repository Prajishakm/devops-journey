# Lab 02 – Python Log Parser

**Goal:** Refresh Python (files, regex, dicts, Counter) with a real sysadmin task.

## Task
Fill in every `TODO` in `log_parser.py` until all tests pass.

```bash
pytest -v                          # red at first – that's the point
python log_parser.py sample_access.log
```

## Stretch goals
- Add `--status 404` CLI option to show only those lines (use `argparse`)
- Run it on a real log: `/var/log/nginx/access.log` or `/var/log/httpd/access_log`
- Top 3 most requested paths
