# CLOUDNANO REMEDIATION PLAN
**Operator:** Shatiqua Talley

---

> Risk is not a score. It is **Likelihood × Impact** — assessed against real-world reachability,
> data sensitivity, and exploitability.

---

## TOP 5 CRITICAL FIXES
*(From the 20 raw findings, select the 5 that pose the greatest ACTUAL risk. Explain your reasoning.)*

## Key Engineering Considerations

1. *Likelihood of exploitation*
2. *Internet-facing accessibility*
3. *Exposure of sensitive customer or HR data*
4. *Potential for privilege escalation or lateral movement*
5. *Operational and reputational business impact*   

---

1. **Unauthenticated AWS S3 Bucket (Contains Customer PII)**   
[CVSS 9.8]  
   * **Justification:** 

		> **Public access** = immediate likelihood   
		> **Customer PII** = regulatory disaster  

> **Likelihood:** High, because the storage bucket is publicly accessible without authentication and can be reached by any external actor.
>
> **Impact:** Severe, because the exposed data includes customer PII, creating immediate regulatory, legal, and reputational damage.

2. **SQL Injection in Login Page (Customer Database Portal)**   
[CVSS 8.1]  
   * **Justification:** 

		> **Internet-facing login** = constant attack surface  
		> **Database access** = full customer records

> **Likelihood:** High, because the vulnerability exists on an internet-facing login page that attackers can reach directly.
>
> **Impact:** Severe, because successful exploitation allows unauthorized access to the core customer database.

3. **Remote Code Execution in Apache Struts (Internet Facing Web Server)**   
[CVSS 9.8]  
   * **Justification:** 

		> **Internet-facing web server** = universal reachability  
		> **Remote code execution** = full system control

> **Likelihood:** High, because the vulnerable service is publicly exposed and has known exploitation methods.
>
>**Impact:** Critical, because remote code execution enables full system takeover and further network compromise.

4. **SMBv1 Enabled (Internal HR File Server)**   
[CVSS 9.0]  
   * **Justification:** 

		> **Active network use** = reliable reach once breached  
		> **HR PII/payroll data** = massive compliance risk

> **Likelihood:** Moderate, because exploitation requires initial internal access but is commonly chained after phishing or credential compromise.
> 
> **Impact:** High, because SMBv1 enables lateral movement and ransomware propagation across sensitive HR systems.

5. **Cross-Site Scripting (XSS) on Support Forum**  
[CVSS 8.8]  
   * **Justification:** 

		> **Public customer forum** = constant user interaction  
		> **Session theft** = account compromise cascade

> **Likelihood:** High, because the support forum is internet-facing and accepts user-generated content.
>
>**Impact:** High, because XSS can be used to hijack sessions and compromise customer accounts.

### Triage Logic Summary
The remediation strategy follows the engineering risk formula:

```text
Risk = Likelihood x Impact
```
