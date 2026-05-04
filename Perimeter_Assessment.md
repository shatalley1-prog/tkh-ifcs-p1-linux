# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator:Shatiqua Talley ** **Target Subnet:** 172.88.0.0/24

## PHASE 1: ACTIVE ENUMERATION (NMAP)
*(List the live IPs discovered and their running services/versions)*
* **Host 1 (172.88.0.10):** nginx 1.14.2 (HTTP on port 80)
* **Host 2 (172.88.0.15):** No open ports detected (host active)
* **Host 3 (172.88.0.20):** Apache httpd 2.4.66 (HTTP on port 80)

## PHASE 2: VULNERABILITY AUDIT (NIKTO)
*(Run Nikto against the TWO web servers discovered above. List one major finding for each.)*
* **Web Server 1 Finding:** Missing X-Frame-Options header allows potential clickjacking attacks (Nikto)
* **Web Server 2 Finding:** HTTP TRACE method enabled, allowing potential Cross-Site Tracing (XST) attacks (Nikto)

## PHASE 3: RISK TRIAGE
*(Review your findings. Identify the SINGLE highest-risk vulnerability across the entire DMZ. Justify why it is the top priority using the Likelihood x Impact formula.)*

* **Top Priority Remediation:** HTTP TRACE method enabled on Apache server (172.88.0.20)
* **Justification:** This represents the highest risk because the server is internet-facing (Likelihood: High) and the enabled TRACE method can be exploited for Cross-Site Tracing attacks to expose sensitive data (Impact: High).
