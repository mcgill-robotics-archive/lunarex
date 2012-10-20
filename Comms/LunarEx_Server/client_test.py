import socket
HOST, PORT = 'localhost', 5902
# SOCK_STREAM == a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.setblocking(0)  # optional non-blocking
sock.connect((HOST, PORT))
byte=1
while(True):
    byte=byte<<1
    print byte
    data=sock.send(chr(byte))
    if(byte>16):
        byte=1
