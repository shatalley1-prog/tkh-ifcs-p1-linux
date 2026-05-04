# TARGET THREAT PROFILE: CloudNano 
**Classification:** Passive Security Audit  
**Operator:** Shatiqua Talley   

---

> **Mission:** Build a clear threat profile using passive OSINT findings only.

---

## 1. Subdomain Discovery   
* **Tool Used:** `Sublist3r`  
* **Target Domain:** `tesla.com` (Proxy for CloudNano)  
* **Subdomains Found:**   
 
	* `accounts.tesla.com` (Authentication & Identity)  
	* `toolbox.tesla.com` (Diagnostics & Internal Tools)  

**Notes:** These subdomains suggest significant public-facing login and internal-tool surfaces.

## 2. Tech Stack Mapping     
* **Tool Used:** BuiltWith / Wappalyzer  
* **Identified Technologies (CMS/CDN/Backend):**   

| Layer | Technology | Description |
| :--- | :--- | :--- |
| **Frontend Framework** | Next.js | React-based SSR framework |
| **Data Visualization** | Plotly | Interactive analytics dashboards |
| **Operating System** | Ubuntu | Linux-based backend OS |

### Additional Observations    

	- Pages are optimized for mobile compatibility  
	- Heavy reliance on JavaScript-based rendering  
	- Use of third‑party protection such as CAPTCHA  

### Observations  
The site appears to use a modern web framework and analytics-style tools.  

## 3. Major Exposure Points & Dangers   
*(List three major exposure points discovered during your OSINT audit and explain why they are dangerous)*

1. **Authentication Surface (`accounts.tesla.com`):**   
The use of **Next.js** indicates a modern, fast user interface for logins. However, because this site handles identity management, it is a primary target for **Server-Side Request Forgery (SSRF)** or vulnerabilities in the way the framework handles server-side rendering (SSR) of user accounts.  

2. **Internal Diagnostic Data (toolbox.tesla.com):**   
This subdomain leverages **Plotly**, which points to the handling of highly detailed vehicle telemetry and engineering data. Exposure of this portal could allow an attacker to view proprietary performance metrics or even vehicle-specific logs.  

3. **OS & Location Footprint:**   
The infrastructure is confirmed to run on **Ubuntu**, with servers located in regions like **Finland and the UAE**. Knowing the specific OS allows attackers to hunt for known kernel exploits, while the diverse server locations increase the complexity of maintaining consistent security patches across the global network.  


