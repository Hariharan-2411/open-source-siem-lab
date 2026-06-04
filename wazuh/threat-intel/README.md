# Threat Intelligence — CDB Lists

## Overview
Wazuh CDB (Constant Database) lists provide fast IOC lookups at rule
evaluation time. These lists are populated from free, publicly available
threat intelligence feeds.

## Feeds

| Feed | Source | Content | Rules |
|------|--------|---------|-------|
| Feodo Tracker | feodotracker.abuse.ch | Botnet C2 IPs | 100020 |
| Manual seeds | Lab | Phishing domains | 100021 |
| Manual seeds | Lab | Malware hashes | 100022 |

## Update Schedule
Daily at 06:00 UTC via cron.
Manual: `sudo bash update-threat-feeds.sh`
Log: `/var/log/threat-feed-update.log`

## Key Notes
- CDB source files have no extension (not .txt)
- Binary .cdb files generated with tinycdb: `cdb -c -m`
- Files must be owned by wazuh:wazuh
- .cdb binary files are excluded from git via .gitignore
