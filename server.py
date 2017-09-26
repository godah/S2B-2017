import socket
import sys

HOST = None               
PORT = 50007
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print( 'could not open socket')
    sys.exit(1)
conn, addr = s.accept()
print('Connected by', addr)
while 1:
    data = conn.recv(1024)
    print(repr(data))
    if not data: break
    if sys.platform == "win32":
        info = ''.join(map(str, sys.getwindowsversion()))	
        conn.send(str.encode("Send from Server: Plataform:"+sys.platform +" winInfo:"+ info +" Winver: "+ sys.winver))
		
    else:
        conn.send(str.encode("Send from Server: Platform: " + sys.platform()))
conn.close()