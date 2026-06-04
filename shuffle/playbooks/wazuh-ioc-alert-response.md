# Wazuh IOC Alert Response Playbook

## Trigger
Wazuh rule 100020 — IOC match: known malicious IP

## Webhook URL
http://localhost:3001/api/v1/hooks/webhook_8e649154-a989-4798-aa02-1e6dae10e6a0

## Workflow Steps
1. Webhook receives Wazuh alert JSON
2. Shuffle Tools parses alert fields
3. Produces structured IR log entry:
   - Rule ID
   - Description
   - Source IP
   - Agent name
   - Timestamp

## MITRE ATT&CK
- T1071 Command and Control
- T1078 Valid Accounts

## Data Fields Used
- $exec.rule_id
- $exec.title
- $exec.all_fields.data.srcip
- $exec.all_fields.agent.name
- $exec.timestamp
