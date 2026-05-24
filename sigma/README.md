# Sigma Rules

Vendor-neutral detection rules written in Sigma format.
These rules can be converted to any SIEM platform.

## Rules

| File | Detects | MITRE | Wazuh Rule ID |
|---|---|---|---|
| credential_discovery_sudo.yml | sudo cat /etc/passwd or /etc/shadow | T1087, T1003 | 100001 |
| ssh_brute_force.yml | 8+ failed SSH logins from same IP in 2min | T1110.001 | 100002 |
| sudo_abuse.yml | Suspicious commands run as root via sudo | T1548.003, T1059 | 100003 |
| log_tampering.yml | sudo rm/shred/truncate of /var/log | T1070.002 | 100004 |

## Conversion Notes

### Sigma to Wazuh XML mapping
| Sigma field | Wazuh equivalent |
|---|---|
| level: high | rule level="12" |
| level: critical | rule level="14" |
| data.command\|contains: x | \<field name="command"\>x\</field\> |
| tags: attack.tXXXX | \<mitre\>\<id\>TXXXX\</id\>\</mitre\> |
| logsource.service: sudo | \<if_group\>sudo\</if_group\> |

### Why both formats exist
- Sigma: universal, shareable, platform-agnostic documentation
- Wazuh XML: platform-specific, actually deployed and running
- In a real SOC: write Sigma first, convert to platform format second

## Tools
- sigma-cli 3.0.2 installed at /home/ubuntu/.local/bin/sigma
- Wazuh backend plugin not available for sigma-cli 3.x
- Conversion done manually using field mapping table above
