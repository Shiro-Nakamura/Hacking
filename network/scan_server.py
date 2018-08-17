import socket

HOST = "127.0.0.1"
PORT = 5000
BUFFER = 1024

socket.setdefaulttimeout(3)
s = socket.socket()
try:
    s.connect((HOST,PORT))
    banner = s.recv(BUFFER)
    print("[+] banner: {}".format(banner))
    
except Exception as e:
    print("[-] Error: "+str(e))

