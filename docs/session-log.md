where# Session Log

## Session 0 — Architecture & Planning
**Date:** 2026-05-15
**Status:** Complete

### What was done
- Defined full 8-layer SIEM pipeline architecture
- Chose tool stack: Wazuh, MISP, Shuffle, Sigma, Atomic Red Team
- Planned VM resource allocation (10-12 GB RAM, 50 GB disk, 4 CPU cores)
- Created GitHub repository structure
- Committed initial docs and folder scaffold

### Key decisions
- Single VM deployment (all components on one Kali Linux machine)
- Wazuh chosen over raw ELK for built-in detection engine
- MISP chosen over OpenCTI for lower RAM footprint
- Shuffle chosen as SOAR for beginner accessibility

### Next session
Session 1 — VM preparation, hardening, snapshot discipline


## Session 1 — VM Preparation (AWS EC2)
**Date:** 2026-05-18
**Host:** AWS EC2 m7i-flex.large, us-east-1
**OS:** Ubuntu 24.04 LTS x86_64

### Completed
- Hostname set to siem-lab
- System fully updated (kernel 6.17.0-1015-aws)
- NTP synchronized (UTC)
- UFW firewall enabled (ports 22, 443, 1514, 1515, 9200)
- File descriptor limit raised to 65536
- Swappiness set to 10
- AWS AMI snapshot: session1-clean-baseline

### Resume Point
Session 2 — Wazuh installation


## Session 2 — Wazuh Installation
**Date:** 2026-05-19
**Status:** Complete

### Completed
- Wazuh Indexer 4.14.5 installed and running
- TLS certificates generated for all components
- Wazuh Manager 4.14.5 installed and running
- Filebeat configured and shipping alerts
- Wazuh Dashboard accessible at https://54.82.59.160
- 348 alerts already detected on first run

### Services Running
- wazuh-indexer: active
- wazuh-manager: active
- wazuh-dashboard: active
- filebeat: active

### Resume Point
Session 3 — Log sources and Wazuh agent

# Session 3: Log Sources & Wazuh Manager

## What Was Accomplished
- Diagnosed and fixed Wazuh Manager broken installation
  (missing binaries due to manager/agent package conflict)
- Added 4GB swap file to prevent OOM kills of wazuh-indexer
- Extended systemd timeout for wazuh-indexer to 180s
- Created systemd service unit for wazuh-manager (Type=oneshot)
- Configured auth block in ossec.conf to enable port 1515
- Registered agent ID 001 (siem-lab-ubuntu) via manage_agents
- Verified all critical manager daemons running:
  analysisd, remoted, authd, db, execd, logcollector, monitord
- Verified ports 1514 and 1515 open and listening
- Dashboard confirmed active: 675+ alerts from self-monitoring

## Architecture Learned
- wazuh-manager and wazuh-agent are mutually exclusive packages
- Single-VM: manager self-monitors via ID 000 natively
- Agent registration uses port 1515 (authd) for key exchange
- Agent communication uses port 1514 (remoted) for log shipping
- client.keys stores cryptographic identity for each agent

## Key Files Modified
- /var/ossec/etc/ossec.conf — added <auth> block
- /etc/systemd/system/wazuh-manager.service — created unit file
- /etc/systemd/system/wazuh-indexer.service.d/override.conf — timeout
- /var/ossec/etc/client.keys — agent 001 registered
- /swapfile — 4GB swap added permanently

## Troubleshooting Learned
- Stale PID files cause "already running" false positives
  Fix: sudo rm -f /var/ossec/var/run/*.pid
- wazuh-indexer dies with status=143 = systemd timeout
  Fix: TimeoutStartSec=180 in override.conf
- manager/agent package conflict is by design, not a bug
  Fix: use manage_agents for manual registration

## MITRE ATT&CK Relevance
- T1078 Valid Accounts: auth.log captures login events
- T1110 Brute Force: failed SSH attempts trigger alerts
- T1136 Create Account: useradd/adduser logged and alerted

## Next Session
Session 4: Log parsing and normalization deep dive
- How Wazuh decoders extract fields from raw log lines
- Writing custom decoders for application logs
- Understanding alert rule levels and groups


# Session 4: Log Parsing, Decoders & Detection Engineering

## Status: COMPLETE

## What Was Accomplished
- Traced a real alert end-to-end: raw log → decoder → rule → alert → OpenSearch → Dashboard
- Read Wazuh sudo decoder chain (0320-sudo_decoders.xml) line by line
- Read rule 5402/5403 including MITRE ATT&CK mapping
- Used wazuh-logtest to test rules interactively
- Wrote custom detection rule 100001 from scratch
- Debugged rule chaining: if_sid vs if_group vs field matching
- Confirmed rule fired on live system via alerts.log
- Queried OpenSearch directly to see alert JSON document
- Verified 1171 alerts stored in OpenSearch filing room

## The Full Pipeline
sudo cat /etc/passwd (typed by user)
        ↓
/var/log/auth.log (Linux wrote it)
        ↓
wazuh-logcollector (picked it up, shipped to analysisd)
        ↓
Decoder (broke raw text into named fields)
        ↓
Rule engine (matched rule 100001 on command field)
        ↓
alerts.log (alert written)
        ↓
Filebeat (picked up, packaged as JSON, shipped to OpenSearch)
        ↓
OpenSearch (indexed into wazuh-alerts-4.x-2026.05.22)
        ↓
Dashboard (read from OpenSearch, displayed to analyst)

## Key Concepts
- Decoder parent: identifies log source via program_name
- Decoder child: extracts fields via regex capture groups
- Rule if_sid: chain on specific rule ID
- Rule if_group: chain on any rule in a group (more flexible)
- Rule field name="x": match decoded field (always prefer over regex)
- Custom rules start at ID 100000
- OpenSearch index per day: wazuh-alerts-4.x-YYYY.MM.DD
- Alert JSON contains: predecoder, agent, data, rule sections

## Custom Rule Written
Rule 100001 - level 10
Detects: sudo cat of /etc/passwd or /etc/shadow
MITRE: T1087 Account Discovery, T1003 OS Credential Dumping
File: wazuh/rules/local_rules.xml

## Debugging Lessons
1. if_sid fails when a different child rule wins first
2. regex on raw log unreliable after rule chaining
3. field name="command" reliable — always matches decoded value
4. wazuh-logtest is your best friend for testing before deploying

## IR Analyst Relevance (Vosyn)
T1087 + T1548.003 together = privilege escalation then discovery
This pattern = active post-exploitation. Escalate immediately.
Real investigation checklist:
- Is this user supposed to have sudo? 
- First time using it? (FTS = higher suspicion)
- What exact command? (/etc/shadow = critical)
- What time? After hours = escalate
