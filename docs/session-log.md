# Session Log

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
