import nmap
scanner = nmap.PortScanner()
scanner.scan("89.43.3.0/24", "1-256", '-v -sS -sV')
result = ""
for ip in scanner.all_hosts():
    try:
        for port in scanner[ip]['tcp'].keys():
            probe_result = f"{ip}:{port} runs {scanner[ip]['tcp'][port]['product']} version {scanner[ip]['tcp'][port]['version']}"
            print(probe_result)
            result += probe_result + "\n"
    except:
        pass
    print("--------")
    result += "--------" + "\n"
f = open("result_serviceprobe.txt", "w")
f.write(result)
f.close()