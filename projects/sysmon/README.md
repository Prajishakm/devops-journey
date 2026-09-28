# sysmon – capstone project

A tiny system monitor that I extend in every phase of my DevOps journey.

| Version | Phase | What's new |
|---|---|---|
| v1 | Refresh | Python CLI, psutil, SQLite, alerts ← **now** |
| v2 | Containers | Dockerfile, docker-compose, Kubernetes manifests |
| v3 | Cloud | Runs on Azure (VM or Container Apps) |
| v4 | IaC + CI/CD | Terraform + GitHub Actions auto-deploy |
| v5 | Monitoring + AI | Prometheus exporter, Grafana dashboard, AI anomaly summary |

## v1 task
Fill the `TODO`s in `sysmon.py` until `pytest -v` is green.

```bash
python sysmon.py collect --every 5   # Ctrl+C after a while
python sysmon.py report
```

Test an alert: `stress --cpu 4 --timeout 20` (install with `dnf install stress`) in another terminal.
