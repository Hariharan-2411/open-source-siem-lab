# Open-Source SIEM Lab

A fully functional, end-to-end SIEM pipeline built on a single VM.

## Architecture

> Wazuh (SIEM/XDR) → OpenSearch (Indexer) → Wazuh Dashboard →
> MISP (Threat Intel) → Shuffle (SOAR)

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
| 1 | VM Preparation | ⬜ Pending |
| ... | ... | ... |

## MITRE ATT&CK Coverage

*(To be populated as detections are built)*
