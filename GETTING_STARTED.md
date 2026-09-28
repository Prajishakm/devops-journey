# Getting started – put this on GitHub

## 1. One-time Git setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 2. Create the repo
1. github.com → **New repository** → name: `devops-journey` → Public → *don't* add a README → Create
2. In this folder:
```bash
git init
git add .
git commit -m "Initial structure: topics, notes and Phase 1 labs"
git branch -M main
git remote add origin https://github.com/<your-username>/devops-journey.git
git push -u origin main
```
(GitHub asks for a **Personal Access Token** instead of a password: Settings → Developer settings → Tokens.)

## 3. Daily workflow – one commit per small step
```bash
pytest -v 04-python/labs/lab01-log-parser     # work until green
git add 04-python/labs/lab01-log-parser
git commit -m "lab02: parse_line and top_ips working"
git push
```
Then tick the box in the main README ✅.

Recruiters look at your **commit history** – small, regular commits with clear messages show real learning.

## Suggested Week 1–4 schedule
| Week | Do |
|---|---|
| 1 | Git setup + push repo · 01-linux sessions 1–2 |
| 2 | 01-linux sessions 3–5 · 02-bash lab01 |
| 3 | 04-python concepts + lab01-log-parser |
| 4 | 05-sql lab01-api-to-sqlite · projects/sysmon v1 |
