# TARGET THREAT PROFILE: CloudNano 
**Classification:** Passive Security Audit  
**Operator:** Shatiqua Talley   

**Mission:** Build a clear threat profile using passive OSINT findings only.

---

The following digital footprint analysis provides a comprehensive technical audit of the specified targets to assess potential risks associated with the TitanCorp acquisition.

---

## 1. Subdomain Discovery   
* **Tool Used:** `Sublist3r`  
* **Target Domain:** `tesla.com` (Proxy for CloudNano)  
* **Subdomains Found:** 40   

Highest‑impact components of the target’s identity:

| Subdomain                          | Purpose                                      | Risk Level |
| ---------------------------------- | -------------------------------------------- | ---------- |
| `accounts.tesla.com`               | Identity Gateway — logins, passwords, tokens | Critical   |
| `sso-dev.tesla.com`                | Development Single Sign-On                   | Critical   |
| `auth.tesla.com`                   | Main Authentication System                   | Critical   |
| `mfa-reset.tesla.com`              | MFA Reset Interface                          | Critical   |
| `fleet-api.prd.vn.cloud.tesla.com` | Production Fleet API                         | Critical   |

## 2. Tech Stack Mapping     
* **Tool Used:** BuiltWith / Wappalyzer  
* **Identified Technologies (CMS/CDN/Backend):**   

### CMS

| Technology | Found On |
| ---------- | -------- |
| Drupal 9 | auth.tesla.com, sso-dev.tesla.com, fleet-api.prd.vn.cloud.tesla.com |
| Next.js | accounts.tesla.com, sso-dev.tesla.com |

No traditional CMS is used for identity or API logic across these subdomains.
CMS technologies (e.g., Drupal) detected at the organizational level apply to general site content, not to authentication flows or APIs.
Identity and API services are implemented as custom applications, which is expected for security‑critical systems.

### CDN

| Technology | Found On |
| ---------- | -------- |
| Akamai Edge | auth.tesla.com, sso-dev.tesla.com, fleet-api.prd.vn.cloud.tesla.com |
| Akamai | mfa-reset.tesla.com |

Akamai CDN and edge services are consistently present across the stack (including Akamai Edge, Bot Manager, and performance monitoring).
This provides global delivery, DDoS mitigation, and abuse controls in front of all public endpoints.

### Backend Technologies

| Technology | Found On |
| ---------- | -------- |
| nginx + Apache | auth.tesla.com, sso-dev.tesla.com, fleet-api.prd.vn.cloud.tesla.com |
| Amazon AWS | auth.tesla.com, sso-dev.tesla.com, fleet-api.prd.vn.cloud.tesla.com |
| Linux | auth.tesla.com, sso-dev.tesla.com, fleet-api.prd.vn.cloud.tesla.com |
| Docker + Kubernetes | auth.tesla.com, sso-dev.tesla.com, fleet-api.prd.vn.cloud.tesla.com |
| MongoDB + MySQL | auth.tesla.com, sso-dev.tesla.com, fleet-api.prd.vn.cloud.tesla.com |
| React + JavaScript | accounts.tesla.com, fleet-api.prd.vn.cloud.tesla.com |
| Akamai Bot Manager | auth.tesla.com, sso-dev.tesla.com, fleet-api.prd.vn.cloud.tesla.com |

Custom authentication backends for accounts, auth, sso-dev, and mfa-reset, handling credentials, sessions, tokens, and recovery workflows.
Custom, cloud‑hosted REST APIs for fleet-api.prd.vn.cloud.tesla.com, designed for machine‑to‑machine access (no UI, no CMS).
Cloud infrastructure indicators (AWS, containerization, orchestration) support scalable identity and API operations.

## 3. Major Exposure Points & Dangers   
*(List three major exposure points discovered during your OSINT audit and explain why they are dangerous)*

1. Identity Harvesting (accounts.tesla.com)  
These systems control user login, credentials, and session tokens, any weakness here could enable account takeover, expose customer data, and undermine trust in the acquired business.

2. Lateral Movement (sso-dev.tesla.com)   
Exposure of development SSO or production fleet APIs creates a high‑impact risk because it can expose weaker controls and allow attackers to pivot from test access into sensitive internal workflows or permissions.

3. Fleet Sabotage (fleet-api.prd.vn.cloud.tesla.com)  
Unauthorized access to a live production fleet API introduces  immediate safety risk, potential physical harm, and catastrophic regulatory liability, because it can affect live vehicle data or operations at scale, creating immediate safety, legal, and reputational impact.

### Conclusion  
From an acquisition standpoint, the greatest residual risk arises not from content systems, but from identity and fleet‑control services where a single authorization failure could create immediate safety, regulatory, and reputational consequences.

---

All findings were gathered using passive OSINT techniques only.
No packets were sent directly to target systems.

---
