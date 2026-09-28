# Lab 01 – Bash: System Info Report

**Goal:** Warm up your Linux + Bash skills.

## Task
Complete `sysinfo.sh` so it prints:
1. Hostname and current date/time
2. Uptime
3. Disk usage of `/` (used %, available)
4. Memory usage (total / used / free, in MB)
5. Top 5 processes by memory

Then add:
- A `--save` flag that writes the report to `reports/sysinfo-YYYYMMDD-HHMM.txt`
- A warning line `WARNING: disk usage above 80%` when `/` is over 80%

## Hints
`hostname`, `date`, `uptime -p`, `df -h /`, `free -m`, `ps aux --sort=-%mem | head -6`, `awk`, `mkdir -p`

## Done when
```bash
chmod +x sysinfo.sh
./sysinfo.sh
./sysinfo.sh --save && ls reports/
```
Both work, and `shellcheck sysinfo.sh` shows no errors.
