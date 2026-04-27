#!/usr/bin/env python3
"""
==================================================
Session 07 - The Sentry
==================================================
Mission: The Automation Forge
Author: Shatiqua Talley
Environment: Chromebook Linux (Penguin)
Description: Checks SSH port 22 is open on a list of target servers using 
a 1-second timeout to determine whether each server is reachable.
==================================================
Port Checker
==================================================
"""
import socket

# A list of our server IPs
targets = ["127.0.0.1", "8.8.8.8", "1.1.1.1", "10.0.0.1", "100.115.92.193"]

for ip in targets:
    print(f"--- Checking Server: {ip} ---")
    
    # Create a socket to knock on the door
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timer so we don't wait forever
    s.settimeout(1)
    
    # Knock on Port 22 (SSH)
    result = s.connect_ex((ip, 22))
    
    # 0 means Open, anything else means Closed
    if result == 0:
        print(f"SUCCESS: Port 22 is OPEN on {ip}")
    else:
        print(f"FAILED: Port 22 is CLOSED on {ip}")
    
    # Close the connection
    s.close()
