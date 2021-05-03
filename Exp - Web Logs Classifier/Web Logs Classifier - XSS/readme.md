**Logs created from DVWA.**

Injection into GET request generated from XSS page <code>/DVWA/vulnerabilities/xss_r/?name=xxx</code>

Normal Logs:
1. Injecting <code>/usr/share/wordlists/wfuzz/general/medium.txt</code>
2. Injecting <code>/usr/share/wordlists/wfuzz/others/names.txt</code>

Malicious Logs (from https://github.com/payloadbox/xss-payload-list):
1. Injecting <code>/xss-payload-list-master/Intruder/xss-payload.txt</code> 
2. Injecting <code>XSS_2.txt</code> 


