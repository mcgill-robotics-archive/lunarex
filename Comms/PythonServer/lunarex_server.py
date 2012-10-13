import socket
import sys
import serial
from math import fabs
from threading import Thread

HOST=''
PORT=31092
BUFFERSIZE=4096

ser=serial.Serial('/dev/ttyACM0',9600)    
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

if __name__ == '__main__':
    s.bind(('',31092))
while 1:
    try:    
        print "Waiting for a connection...\n"
        s.listen(5)
        (client,address)=s.accept()
        while 1:
            try:
                    data=client.recv(1)
                    print data,
            except:
                print "Error occurred. "
                break
    except IOError:
        print "Client crashes. Keep waiting for the next connection...\n"
        continue
