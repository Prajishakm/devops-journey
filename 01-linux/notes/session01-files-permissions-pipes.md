# Session 1 – Files, permissions, pipes

## 1. Navigation & files
```bash
pwd                     # where am I
cd ~ && mkdir -p practice/logs && cd practice
touch app.log notes.txt
ls -lah                 # hidden files + human-readable sizes
cp app.log logs/ && mv notes.txt readme.txt
find . -name "*.log"    # search files
```

## 2. Permissions
`-rwxr-xr--` → 3 groups: **owner / group / others**

| Letter | Value | Meaning |
|---|---|---|
| r | 4 | read |
| w | 2 | write |
| x | 1 | execute |

`rwx`=7, `r-x`=5, `r--`=4 → `chmod 754 file`
```bash
chmod 750 app.log
chmod +x script.sh
sudo chown root:root app.log
```

## 3. Pipes & redirection
| Syntax | Meaning |
|---|---|
| `>` | write output (overwrite) |
| `>>` | append output |
| `2>` | write errors |
| `> out 2>&1` | output + errors to same file |
| `\|` | output of left → input of right |
| `/dev/null` | "black hole", throw away |

```bash
echo "hello" > file.txt
echo "world" >> file.txt
cat file.txt | wc -l
ps aux | grep sshd
ls /nonexistent 2> err.txt
```

## 4. Daily commands
`df -h` disk · `du -sh *` folder sizes · `free -m` memory · `head -5 file` · `tail -f file` (follow live log)

## My notes
<!-- Write what you learned / what confused you here -->
