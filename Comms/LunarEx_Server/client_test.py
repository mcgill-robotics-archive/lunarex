import socket
HOST, PORT = 'localhost', 31092
# SOCK_STREAM == a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.setblocking(0)  # optional non-blocking
sock.connect((HOST, PORT))
while(True):
    data=sock.recv(1024)
    print data
