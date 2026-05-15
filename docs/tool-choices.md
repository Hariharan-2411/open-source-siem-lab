# Tool Choices

## Wazuh (SIEM Core)
- **What:** Open-source SIEM and XDR platform
- **Why:** Unlimited data, full detection engine, used in real SOCs and MSSPs
- **Replaces:** Splunk (500MB/day cap, no detection engineering), raw ELK (no detection layer)
- **Market relevance:** Cited in SOC analyst job postings, comparable workflow to Microsoft Sentinel and IBM QRadar

## MISP (Threat Intelligence)
- **What:** Open-source Threat Intelligence Platform for managing IOCs
- **Why:** Leaner than OpenCTI, direct Wazuh integration, real SOC habit
- **Replaces:** Text-file threat feeds (no deduplication, no scoring)
- **Market relevance:** Used by CERTs, financial institutions, and government SOCs worldwide

## Shuffle (SOAR)
- **What:** Open-source Security Orchestration, Automation and Response platform
- **Why:** Beginner-accessible, handles automation layer (playbooks, webhooks, API integrations)
- **Replaces:** TheHive/DFIR-IRIS (those are case management, not automation)
- **Market relevance:** Concepts transfer directly to Palo Alto XSOAR and Microsoft Sentinel Logic Apps

## Sigma (Detection Rules)
- **What:** Vendor-neutral YAML rule format for log-based detections
- **Why:** Lingua franca of detection engineering, converts to any SIEM
- **Market relevance:** Referenced in MITRE ATT&CK, used by threat researchers after major breaches

## Atomic Red Team (Attack Simulation)
- **What:** Library of small ATT&CK-mapped attack simulations
- **Why:** No server required, validates whether detections actually fire
- **Replaces:** Caldera/VECTR (heavier, overkill for single VM)
- **Market relevance:** Standard reference for purple team exercises