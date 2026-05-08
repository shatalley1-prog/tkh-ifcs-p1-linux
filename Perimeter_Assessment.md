# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator: Shatiqua Talley ** 

**Target Subnet:** 172.88.0.0/24

---

**Mission:** To perform a full-scope reconnaissance and vulnerability assessment of this subnet.

---

## PHASE 1: ACTIVE ENUMERATION (NMAP)

**Goal:** Identify live assets without triggering alarms.

Ordered execution flow:

1. Ping Sweep performed:

   ```bash
   nmap -sn 172.88.0.0/24
   ```

2. Aggressive version scan performed:

   ```bash
   sudo nmap -sV 172.88.0.10 172.88.0.15 172.88.0.20

*(List the live IPs discovered and their running services/versions)*

* **Host 1 (172.88.0.10):** nginx 1.14.2 (HTTP on port 80)
* **Host 2 (172.88.0.15):** No open ports detected (host active)
* **Host 3 (172.88.0.20):** Apache httpd 2.4.66 (HTTP on port 80)

> **Note:** Host 172.88.0.1 responded to the sweep but was identified as 
> the network gateway and excluded from further vulnerability auditing.

## PHASE 2: VULNERABILITY AUDIT (NIKTO)

**Goal:** Scan the web applications for misconfigurations.

*(Run Nikto against the TWO web servers discovered above. List one major finding for each.)*

Audit command used: `nikto -h http://[TARGET_IP]

* **Web Server 1 Finding: Outdated `nginx 1.14.2`**

**(172.88.0.10 — nginx 1.14.2):** The server is running *nginx 1.14.2*, a version released in 2018 and no longer receiving 
security patches — flagged by Nikto as outdated software with known CVE exposure.

>Additional observations included a **missing X‑Frame‑Options header** and **ETag inode information leakage**.

* **Web Server 2 Finding: HTTP `TRACE` method enabled**

**(172.88.0.20 — Apache 2.4.66):** The **HTTP TRACE method is active**, flagged by Nikto as `OSVDB-877`, confirming vulnerability 
to Cross-Site Tracing (XST) attacks capable of stealing session cookies and 
authentication headers.

>Additional observations included **multiple HTTP methods exposed** and a **missing X‑Frame‑Options header**.

## PHASE 3: RISK TRIAGE

**Goal:** Prioritize your findings for the CISO.

*(Review your findings. Identify the SINGLE highest-risk vulnerability across the entire DMZ. Justify why it is the top priority using the Likelihood x Impact formula.)*

* **Top Priority Remediation:** 
  **Outdated `nginx 1.14.2` on `172.88.0.10`**
* **Justification:** This represents the highest risk because the **likelihood** of exploitation is extremely high due to the abundance of public exploit code targeting this 2018 software version, and the **impact** is critical as a successful breach could lead to full remote code execution, unauthorized data access, or a persistent foothold within the network.

## SECURITY SUMMARY

-Unnecessary HTTP methods expand attack surface

-Outdated software introduces known CVE exposure

-Missing security headers reduce browser security protections 
