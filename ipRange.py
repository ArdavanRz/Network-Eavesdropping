#9631412
import nmap as np
import portscan

print("enter your desired IP for live host search :")
ip = input()
nmapped = np.PortScannerAsync()
global result
for scan in nmapped.scan(hosts=ip + '24', arguments="-sn") :
    if int(scan[1]["nmap"]['scanstats']['uphosts']) :
        live_hosts = f'{scan[0]} is live'
        print(live_hosts)
        result += str(live_hosts)
print(result)
