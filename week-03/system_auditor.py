#!/usr/bin/env python3
"""
==================================================
Session 09: The Conductor (Functional Automation)
==================================================
Phase 2: The Deep Dive "The Automated Reporter" 
Operator: Shatiqua Talley
Environment: Google CloudShell

Goal: Build a script that audits the system and alerts on threats.
Description: This script scans running processes for threats and logs unauthorized activity to a JSON alert file.
==================================================
System Auditor 
==================================================
"""
import subprocess
import json
import os

print("[*] Initiating System Audit...")

# INSTRUCTION 1: Use subprocess.run() to execute 'ps aux'
# YOUR CODE HERE:
process_list = subprocess.run(["ps", "aux"], capture_output=True, text=True)

# INSTRUCTION 2: Search the captured output for the malicious process
# YOUR CODE HERE:
if "unauthorized_cryptominer" in process_list.stdout:
    print("[!] Alert: Unauthorized process detected!") # This confirms the 'if' statement worked

# INSTRUCTION 3: If found, create a dictionary and save it to 'security_alert.json'
# YOUR CODE HERE:
# Create the data structure
    alert_data = {
        "event": "Unauthorized Process",
        "severity": "High",
        "process": "unauthorized_cryptominer"
    }

    # Open the file in 'w' (write) mode and dump the dictionary into it
    with open("security_alert.json", "w") as file:
        json.dump(alert_data, file, indent=4)
    print("[!] Alert generated: security_alert.json") # This confirms the file export worked

print("[+] Audit Complete.")
