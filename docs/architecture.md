┌─────────────────────────────────────────────────────────────────────┐
│                        YOUR SINGLE KALI VM                          │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                     LAYER 1 — LOG SOURCES                    │   │
│  │                                                              │   │
│  │   Linux syslogs   Auth logs   Web server logs   Simulated    │   │
│  │   /var/log/*      /var/log/   (Apache/Nginx)    Entra ID     │   │
│  │                   auth.log                      JSON samples │   │
│  └──────────────────────────┬───────────────────────────────────┘   │
│                             │                                       │
│                             ▼                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                  LAYER 2 — LOG SHIPPER / AGENT               │   │
│  │                                                              │   │
│  │                     Wazuh Agent (local)                      │   │
│  │         reads log files, forwards to Wazuh Manager           │   │
│  └──────────────────────────┬───────────────────────────────────┘   │
│                             │                                       │
│                             ▼                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │            LAYER 3 — INGESTION, PARSING & NORMALIZATION      │   │
│  │                                                              │   │
│  │                  Wazuh Manager + Wazuh Indexer               │   │
│  │     Receives logs → decodes fields → applies rules →         │   │
│  │     stores normalized events in OpenSearch (Indexer)         │   │
│  └──────────────────────────┬───────────────────────────────────┘   │
│                             │                                       │
│                             ▼                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │              LAYER 4 — DETECTION ENGINEERING                 │   │
│  │                                                              │   │
│  │       Wazuh Rules (XML) + Sigma Rules (converted)            │   │
│  │       Every rule tagged to MITRE ATT&CK technique            │   │
│  └──────────────────────────┬───────────────────────────────────┘   │
│                             │                                       │
│                             ▼                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │               LAYER 5 — ALERTING & DASHBOARDS                │   │
│  │                                                              │   │
│  │              Wazuh Dashboard (built on OpenSearch            │   │
│  │              Dashboards) — your analyst glass pane           │   │
│  └──────────────────────────┬───────────────────────────────────┘   │
│                             │                                       │
│                             ▼                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │            LAYER 6 — THREAT INTELLIGENCE                     │   │
│  │                                                              │   │
│  │                  MISP (lightweight local instance)           │   │
│  │      Feeds IOCs into Wazuh for automated enrichment          │   │
│  └──────────────────────────┬───────────────────────────────────┘   │
│                             │                                       │
│                             ▼                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                LAYER 7 — SOAR / IR WORKFLOW                  │   │
│  │                                                              │   │
│  │                        Shuffle SOAR                          │   │
│  │    Wazuh alert → Shuffle playbook → auto-triage action       │   │
│  └──────────────────────────┬───────────────────────────────────┘   │
│                             │                                       │
│                             ▼                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │              LAYER 8 — ATTACK SIMULATION                     │   │
│  │                                                              │   │
│  │     Atomic Red Team (local) + manual attacks from            │   │
│  │     secondary Kali desktop (optional but powerful)           │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
