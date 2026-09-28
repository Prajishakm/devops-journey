#!/usr/bin/env bash
# Lab 01 – System info report
# Usage: ./sysinfo.sh [--save]
set -euo pipefail

report() {
  echo "=== System Report ==="
  echo "Host: $(hostname)"
  echo "Date: $(date '+%Y-%m-%d %H:%M')"

  # TODO 1: print uptime (hint: uptime -p)

  # TODO 2: disk usage of / (hint: df -h / | awk 'NR==2 {print $5, $4}')

  # TODO 3: memory total/used/free in MB (hint: free -m)

  # TODO 4: top 5 processes by memory (hint: ps aux --sort=-%mem | head -6)

  # TODO 5: if disk usage of / > 80, print "WARNING: disk usage above 80%"
  #         (hint: df --output=pcent / | tail -1 | tr -dc '0-9')
}

if [[ "${1:-}" == "--save" ]]; then
  # TODO 6: mkdir -p reports and save output to reports/sysinfo-$(date +%Y%m%d-%H%M).txt
  echo "--save not implemented yet"
else
  report
fi
