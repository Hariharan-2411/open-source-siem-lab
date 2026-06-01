#!/bin/bash
# update-threat-feeds.sh
# Downloads latest IOC feeds and refreshes Wazuh CDB lists
# Run: sudo bash /var/ossec/etc/lists/threat-intel/update-threat-feeds.sh

set -euo pipefail

LISTS_DIR="/var/ossec/etc/lists"
LOG_FILE="/var/log/threat-feed-update.log"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

echo "[$TIMESTAMP] Starting threat feed update" >> "$LOG_FILE"

FEODO_URL="https://feodotracker.abuse.ch/downloads/ipblocklist.txt"
FEODO_TMP=$(mktemp)

echo "[$TIMESTAMP] Fetching Feodo Tracker IP blocklist..." >> "$LOG_FILE"
if curl -s --connect-timeout 15 --max-time 60 "$FEODO_URL" -o "$FEODO_TMP"; then
    {
        grep -v '^#' "$FEODO_TMP" | grep -v '^$' | grep -E '^[0-9]+\.' | tr -d '\r' | while read -r ip; do
    		echo "${ip}:feodo-tracker"
	done
    } > "${LISTS_DIR}/malicious-ips"
    # Rebuild CDB binary
    grep -v '^#' "${LISTS_DIR}/malicious-ips" | grep -v '^$' | tr ':' '\t' | cdb -c -m "${LISTS_DIR}/malicious-ips.cdb"
    chown wazuh:wazuh "${LISTS_DIR}/malicious-ips" "${LISTS_DIR}/malicious-ips.cdb"
    echo "[$TIMESTAMP] Feodo Tracker update complete" >> "$LOG_FILE"
else
    echo "[$TIMESTAMP] WARNING: Failed to fetch Feodo Tracker feed" >> "$LOG_FILE"
fi
rm -f "$FEODO_TMP"

echo "[$TIMESTAMP] Feed update complete" >> "$LOG_FILE"
echo "---" >> "$LOG_FILE"
