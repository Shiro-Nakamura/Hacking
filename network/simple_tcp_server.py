import socket

HOST = '127.0.0.1'                 
PORT = 5000   
         
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print("[+] start listen on {}".format((HOST,PORT)))
s.listen(1)
conn, addr = s.accept()
banner = 'simple tcp server'
conn.send(banner.encode())
print("[+] connect from address: {}".format(addr))
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()