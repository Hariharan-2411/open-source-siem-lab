# Open-Source SIEM Lab

A fully functional, end-to-end Security Information and Event Management (SIEM) pipeline built on AWS EC2 using open-source tools. Built as a hands-on learning project and portfolio piece by a cybersecurity student and IR analyst.

## Architecture Overview
Log Sources → Wazuh Agent → Wazuh Manager → OpenSearch → Dashboard
↓
Detection Rules
(Custom + Sigma)
↓
Threat Intelligence (CDB Lists)
↓
Shuffle SOAR
(Automated Response)

## Stack

| Component | Tool | Version | Purpose |
|-----------|------|---------|---------|
| SIEM Platform | Wazuh | 4.14.5 | Log ingestion, detection, alerting |
| Search & Storage | OpenSearch | 2.19.5 | Alert indexing and querying |
| Dashboard | Wazuh Dashboard | 4.14.5 | Visualization and threat hunting |
| Log Shipper | Filebeat | 8.x | Alert forwarding to OpenSearch |
| Detection Language | Sigma | 3.0.2 | Vendor-neutral detection rules |
| SOAR | Shuffle | Latest | Automated incident response |
| Infrastructure | AWS EC2 | m7i-flex.large | Ubuntu 24.04 LTS, us-east-1 |

## Detection Coverage

### Custom Wazuh Rules

| Rule ID | Name | MITRE Technique | Level |
|---------|------|----------------|-------|
| 100001 | Credential Discovery | T1087, T1003 | 10 |
| 100002 | SSH Brute Force | T1110.001 | 12 |
| 100003 | Sudo Abuse | T1548.003, T1059 | 12 |
| 100004 | Log Tampering | T1070.002 | 14 |
| 100010 | MFA Fatigue | T1621 | 14 |
| 100011 | High Risk Sign-in | T1078 | 12 |
| 100012 | Credential Stuffing | T1110, T1078 | 13 |
| 100020 | IOC: Malicious IP Match | T1071, T1078 | 14 |
| 100021 | IOC: Malicious Domain Match | T1566, T1071 | 13 |
| 100022 | IOC: Malicious Hash Match | T1204 | 15 |

### MITRE ATT&CK Coverage

| Tactic | Techniques Covered |
|--------|-------------------|
| Credential Access | T1003, T1087, T1110, T1110.001 |
| Privilege Escalation | T1548.003 |
| Defense Evasion | T1070.002 |
| Persistence | T1078 |
| Command & Control | T1071 |
| Initial Access | T1566 |
| Execution | T1059, T1204 |
| Credential Access | T1621 (MFA Fatigue) |

## Threat Intelligence

Live IOC feeds integrated via Wazuh CDB lists:

| Feed | Source | Content |
|------|--------|---------|
| Feodo Tracker | feodotracker.abuse.ch | Botnet C2 IPs (Emotet, QakBot, Dridex) |
| Manual seeds | Lab team | Phishing domains, test hashes |

Auto-updated daily via cron at 06:00 UTC.

## SOAR Automation

Shuffle workflow triggered by rule 100020 (IOC IP match):
Wazuh alert → Shuffle webhook → Parse fields → Structured IR log

Webhook: `http://localhost:3001/api/v1/hooks/webhook_8e649154-a989-4798-aa02-1e6dae10e6a0`

## Repository Structure
├── README.md
├── docs/
│   ├── architecture.md        # Full pipeline diagram
│   ├── session-log.md         # Per-session build log
│   └── tool-choices.md        # Tool selection rationale
├── wazuh/
│   ├── rules/local_rules.xml  # All 10 custom detection rules
│   ├── decoders/              # Custom log decoders
│   ├── configs/ossec.conf     # Manager configuration
│   └── threat-intel/          # CDB lists + feed update script
├── sigma/
│   └── rules/                 # 7 Sigma detection rules
├── shuffle/
│   └── playbooks/             # SOAR workflow documentation
├── log-samples/
│   └── entra-id/              # Simulated Microsoft Entra ID logs
└── screenshots/               # Dashboard and alert screenshots

## Sessions Completed

| Session | Topic | Status |
|---------|-------|--------|
| 0 | Project architecture and tool selection | ✅ |
| 1 | AWS EC2 setup and baseline hardening | ✅ |
| 2 | Wazuh installation and initial config | ✅ |
| 3 | Wazuh manager fix, swap, agent registration | ✅ |
| 4 | Alert pipeline deep dive and logtest | ✅ |
| 5 | Custom detection rules (100001-100004) | ✅ |
| 6 | Sigma rules and sigma-cli | ✅ |
| 7 | Entra ID log simulation and identity rules | ✅ |
| 8 | Dashboard exploration and MITRE mapping | ✅ |
| 9 | Threat intelligence with CDB lists | ✅ |
| 10 | Shuffle SOAR automated response | ✅ |
| 12 | Portfolio finalization | ✅ |

## Infrastructure

- **Cloud**: AWS EC2 m7i-flex.large (2 vCPU, 8GB RAM, 65GB EBS)
- **OS**: Ubuntu 24.04 LTS x86_64
- **Region**: us-east-1
- **Cost management**: Instance stopped between sessions (~$0.17/day storage only)
