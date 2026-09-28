# DevOps Journey 🚀

My hands-on path from Linux admin to DevOps / Cloud Engineer.
Each topic has its own folder with notes, practice and labs I built and tested myself.

## Background
- Red Hat certified (Linux)
- SQL (self-taught)
- Python (refreshing)

## Topics

| # | Topic | Phase | Status |
|---|---|---|---|
| 01 | [Linux](01-linux) | 1 – Foundations | 🟡 In progress |
| 02 | [Bash scripting](02-bash) | 1 – Foundations | ⬜ |
| 03 | [Git & GitHub](03-git) | 1 – Foundations | ⬜ |
| 04 | [Python](04-python) | 1 – Foundations | ⬜ |
| 05 | [SQL](05-sql) | 1 – Foundations | ⬜ |
| 06 | [Docker](06-docker) | 2 – Containers | ⬜ |
| 07 | [Kubernetes](07-kubernetes) | 2 – Containers | ⬜ |
| 08 | [Azure](08-azure) | 3 – Cloud | ⬜ |
| 09 | [Terraform & Ansible](09-terraform-ansible) | 4 – IaC | ⬜ |
| 10 | [CI/CD](10-cicd) | 4 – Automation | ⬜ |
| 11 | [Monitoring & AI](11-monitoring-ai) | 5 – Operate | ⬜ |
| 12 | [Claude (AI for DevOps)](12-claude) | Alongside all phases | ⬜ |

## Projects
- [sysmon](projects/sysmon) – system monitor that grows with every phase (Python → Docker → Azure → Terraform → Grafana)

## How each topic works
1. Read the concept notes (`notes/`)
2. Do the practice tasks (`practice/`)
3. Build the labs (`labs/`) until `pytest` is green
4. Commit and tick the box ✅

## How to run tests
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```
