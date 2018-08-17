import nmap

HOST= '127.0.0.1'
PORTS = ['20','21','22']

def scan(host,port):
    nmap_scan = nmap.PortScanner()
    nmap_scan.scan(host,port)
    state = nmap_scan[host]['tcp'][int(port)]['state']
    print("[*] {} tcp/{} {}".format(host,port,state))
    
    
def main():
        for port in PORTS:
            scan(HOST,port)
        
if __name__ == '__main__':
    main()
    
    
    
    