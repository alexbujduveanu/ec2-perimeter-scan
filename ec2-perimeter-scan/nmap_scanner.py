import nmap

def nmap_scan(ips_and_names_mapping):
    ret = {}
    nm = nmap.PortScanner()
    for name in ips_and_names_mapping.keys():
        ip = ips_and_names_mapping[name]
        print(f'Current IP is {ip}')
        nm.scan(ip, arguments='-Pn -n -p- --host-timeout 10s')
        for host in nm.all_hosts():
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            for proto in nm[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
        
                lport = list(nm[host][proto].keys())
                lport.sort()
                for port in lport:
                    if nm[host][proto][port]['state'] == 'open':
                        print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
                        ret[name] = (ip, port)
    return ret