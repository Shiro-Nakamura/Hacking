import bluetooth as blue
from time import sleep

found_devs = []

def find_devices():
    print("[#] looking for devices")
    dev_list = blue.discover_devices();
    for device in dev_list:
        if device not in found_devs:
            found_devs.append(device)
            name = str(blue.lookup_name(device))
            print("[*] found device name: [{}] [{}]".format(name, device))
            service_discover(device)

    
    
def service_discover(device):
    services = blue.find_service(address=device)
    for service in services:
        name = str(service['name'])
        protocol = str(service['protocol'])
        port = str(service['port'])
        print("[+] found service: [{}][{}][{}]".format(name, protocol, port))
   
def main(): 
    while True:
        find_devices()
        sleep(5)
        
if __name__=="__main__":
    main()