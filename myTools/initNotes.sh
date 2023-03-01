#!/bin/bash
if (($# < 1))
then echo "Usage: initNotes.sh <Name of Box>"
else
mkdir -p $1/{Admin,Deliverables,Evidence/{Findings,Scans/{Vuln,Service,Web,'AD Enumeration'},Notes,OSINT,Wireless,'Logging output','Misc Files'},Retest}
touch $1/Evidence/Findings/{'H1 - Kerberoasting.md','H2 - ASREPRoasting.md','H3 - LLMNR&NBT-NS Response Spoofing.md','H4 - Tomcat Manager Weak Credentials.md'} $1/Evidence/Notes{'1. Administrative Information.md','2. Scoping Information.md','3. Activity Log.md','4. Payload Log.md','5. OSINT Data.md','6. Credentials.md','7. Web Application Research.md','8. Vulnerability Scan Research.md','9. Service Enumeration Research.md','10. AD Enumeration Research.md','11. Attack Path.md','12. Findings.md'}
fi
