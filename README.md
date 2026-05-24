
# Open-Source SIEM Lab

A fully functional, end-to-end SIEM pipeline built on a single AWS EC2 instance.

## Infrastructure
- AWS EC2 m7i-flex.large (2 vCPU, 8GB RAM, 65GB EBS)
- Ubuntu 24.04 LTS x86_64
- Wazuh 4.14.5

## Architecture

Log Sources → Wazuh Agent → Wazuh Manager → OpenSearch → Dashboard
↓
MISP (Threat Intel)
↓
Shuffle (SOAR Playbooks)
See [docs/architecture.md](docs/architecture.md) for the full pipeline diagram.

## Tool Stack

| Layer | Tool | Purpose |
|---|---|---|
| SIEM Core | Wazuh | Log collection, detection, alerting |
| Storage/Search | OpenSearch (Wazuh Indexer) | Event indexing and query |
| Dashboard | Wazuh Dashboard | Analyst glass pane |
| Threat Intel | MISP | IOC management and enrichment |
| SOAR | Shuffle | Automated playbooks |
| Detection Format | Sigma | Vendor-neutral rule writing |
| Attack Simulation | Atomic Red Team | ATT&CK technique validation |

## Session Progress

| Session | Topic | Status |
|---|---|---|
| 0 | Architecture & Planning | ✅ Complete |
| 1 | VM/EC2 Preparation | ✅ Complete |
| 2 | Wazuh Installation | ✅ Complete |
| 3 | Log Sources & Agent | ✅ Complete |
| 4 | Parsing & Detection Engineering | ✅ Complete |
| 5 | Detection Engineering I — Rules + MITRE | ✅ Complete |
| 6 | Sigma Rules | ⬜ Pending |
| 7 | Entra ID Log Simulation | ⬜ Pending |
| 8 | Alerting & Dashboard Engineering | ⬜ Pending |
| 9 | MISP Threat Intelligence | ⬜ Pending |
| 10 | Shuffle SOAR | ⬜ Pending |
| 11 | Atomic Red Team Attack Simulation | ⬜ Pending |
| 12 | Portfolio Finalization | ⬜ Pending |

## MITRE ATT&CK Coverage

| Technique | Description | Rule | Status |
|---|---|---|---|
| T1110.001 | SSH Brute Force | 100002 | ✅ |
| T1548.003 | Sudo Abuse | 100003, 5402 | ✅ |
| T1087 | Account Discovery | 100001 | ✅ |
| T1003 | Credential Dumping | 100001 | ✅ |
| T1070.002 | Log Tampering | 100004 | ✅ |
| T1059 | Command Interpreter | 100003 | ✅ |

## Detection Coverage Map
See [docs/detections/detection-coverage-map.md](docs/detections/detection-coverage-map.md)
