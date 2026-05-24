# OMNI-PORTAL ASSESSMENT REPORT
**Operator:** Shatiqua Talley
**Deadline:** April 5 @ 11:59 PM 

## PHASE 1: AUTH BYPASS (SQLi)
* **Payload Used:** ' OR 1=1– 
* **Result:** Successfully bypassed login and obtained 'auth_token' cookie.

## PHASE 2: CLIENT-SIDE HIJACK (XSS)
* **Stored XSS Payload:** <script>alert(document.cookie)</script>
* **Secret Cookie Captured:** auth_token=SUPPORT_TIER_1_SECRET_TOKEN

## PHASE 3: API ENUMERATION (BOLA)
* **Insecure Order ID:** 501
* **Confidential Data Leaked:**
    "amount": "$15,000.00",
    "details": "Confidential Server Lease",
    "order_id": 501

## PHASE 4: THE REMEDIATION
* **Fix for SQLi:** Implement parameterized queries (prepared statements) for 
all database interactions. Never concatenate user input directly into SQL 
strings. Use server-side validation and ORM query builders to eliminate 
injection at the source.
* **Fix for XSS:** Apply output encoding before rendering any user-supplied 
content in the browser. Sanitize inputs, enforce Content Security Policy (CSP), 
and disable inline JavaScript. Treat all user input as untrusted and escape it 
before inserting into the DOM.
* **Fix for API BOLA:** Enforce strict Access Control Lists (ACLs) and 
server-side authorization checks so users can only access resources they own. 
Before returning order data, verify that the authenticated user's ID matches 
the owner of the requested object. Implement centralized access-control 
middleware to prevent ID enumeration. Replace sequential numeric IDs with 
non-guessable UUIDs to reduce predictability.
