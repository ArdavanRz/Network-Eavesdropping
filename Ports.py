import nmap

nm = nmap.PortScanner()
global result
for i in range(50, 250 + 1):
    res = nm.scan(250, str(i))
    res = res['scan'][250]['tcp'][i]['state']
    result += f'\nport {i} is {res}.\np'

print(result)