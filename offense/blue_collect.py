
import sqlite3
import bluetooth as blue
from time import sleep

found_devs = []
conn = sqlite3.connect('blue.db')
c = conn.cursor()

def find_devices():
    print("[#] looking for devices")
    dev_list = blue.discover_devices();
    for device in dev_list:
        if device not in found_devs:
            found_devs.append(device)
            name = str(blue.lookup_name(device))
            print("[*] found device name: [{}] [{}]".format(name, device))
            t = (device, name)
            c.execute("INSERT INTO blue_devices VALUES (?,?)", t)
            conn.commit()
            
def main():
     while True:
        find_devices()
        sleep(5)
        find_devices()
    
if __name__=="__main__":
    main()