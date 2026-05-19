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
