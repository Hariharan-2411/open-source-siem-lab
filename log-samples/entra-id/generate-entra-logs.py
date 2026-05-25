#!/usr/bin/env python3
import json
import datetime
import time

def write_log(entry):
    with open('/var/log/entra-id/signin.log', 'a') as f:
        f.write(json.dumps(entry) + '\n')

def make_signin(user, ip, country, city, result, risk, mfa_detail, timestamp):
    return {
        "time": timestamp,
        "operationName": "Sign-in activity",
        "resultType": "0" if result == "Success" else "50126",
        "resultDescription": result,
        "userPrincipalName": user,
        "ipAddress": ip,
        "location": {
            "city": city,
            "countryOrRegion": country
        },
        "deviceDetail": {
            "operatingSystem": "Windows 10",
            "browser": "Chrome 120"
        },
        "conditionalAccessStatus": "success",
        "mfaDetail": {
            "authMethod": "Phone app notification",
            "authDetail": mfa_detail
        },
        "riskLevelDuringSignIn": risk,
        "riskLevelAggregated": risk,
        "correlationId": "abc123def456"
    }

now = datetime.datetime.utcnow()

# --- SCENARIO 1: Impossible Travel ---
# Same user logs in from Canada, then Nigeria 3 minutes later
print("Generating Scenario 1: Impossible Travel...")
t1 = now.strftime("%Y-%m-%dT%H:%M:%SZ")
log1 = make_signin(
    user="john.smith@company.com",
    ip="142.150.10.1",
    country="CA",
    city="Toronto",
    result="Success",
    risk="none",
    mfa_detail="MFA completed in Microsoft Authenticator",
    timestamp=t1
)
write_log(log1)
time.sleep(2)

t2 = (now + datetime.timedelta(minutes=3)).strftime("%Y-%m-%dT%H:%M:%SZ")
log2 = make_signin(
    user="john.smith@company.com",
    ip="197.210.50.1",
    country="NG",
    city="Lagos",
    result="Success",
    risk="high",
    mfa_detail="MFA completed in Microsoft Authenticator",
    timestamp=t2
)
write_log(log2)

# --- SCENARIO 2: MFA Fatigue ---
# Same user gets 6 MFA push requests in a row (attacker spamming)
print("Generating Scenario 2: MFA Fatigue...")
for i in range(6):
    t = (now + datetime.timedelta(minutes=10, seconds=i*30)).strftime("%Y-%m-%dT%H:%M:%SZ")
    log = make_signin(
        user="sarah.jones@company.com",
        ip="85.214.100.5",
        country="RU",
        city="Moscow",
        result="MFA denied; user did not respond",
        risk="medium",
        mfa_detail="MFA denied; user did not respond",
        timestamp=t
    )
    write_log(log)

# --- SCENARIO 3: Credential Stuffing Success ---
# 5 failed logins then sudden success from same IP
print("Generating Scenario 3: Credential Stuffing...")
for i in range(5):
    t = (now + datetime.timedelta(minutes=20, seconds=i*10)).strftime("%Y-%m-%dT%H:%M:%SZ")
    log = make_signin(
        user="admin@company.com",
        ip="45.33.100.200",
        country="CN",
        city="Beijing",
        result="Invalid username or password",
        risk="high",
        mfa_detail="MFA not required",
        timestamp=t
    )
    write_log(log)

# Success after failures
t = (now + datetime.timedelta(minutes=21)).strftime("%Y-%m-%dT%H:%M:%SZ")
log = make_signin(
    user="admin@company.com",
    ip="45.33.100.200",
    country="CN",
    city="Beijing",
    result="Success",
    risk="high",
    mfa_detail="MFA bypassed",
    timestamp=t
)
write_log(log)

print("Done. Logs written to /var/log/entra-id/signin.log")
