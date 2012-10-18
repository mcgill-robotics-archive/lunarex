import SocketServer
import sys
import serial
import json
import time
from threading import Thread

HOST=''
PORT=31092
BUFFERSIZE=4096

class Data:
    def __init__(self,x,y,theta):
        self.x=x
        self.y=y
        self.theta=theta

class Handler(SocketServer.BaseRequestHandler):

    def setup(self):
        self.currentState = Data(0.0,0.0,0.0)
        self.initialTime = int(time.time()*1000.0)
        self.currentTime = int(time.time()*1000.0)
        self.request.setblocking(0)

    def handle(self):
        while(True):
            # self.request is the client connection
            try:
                '''
                data = self.request.recv(1024)
                print data
                if(data=='bye'):
                    return
                '''
                
                self.currentTime = int(time.time()*1000.0)
                if((self.currentTime-self.initialTime) > 500):
                    dataPacket = json.dumps(vars(self.currentState),sort_keys=True,indent=4)
                    self.request.send(dataPacket)
                    self.initialTime = int(time.time()*1000.0)
                    print dataPacket

            except:
                pass

    def finish(self):
        self.request.close()

class Server(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)

if __name__ == "__main__":
    server = Server((HOST, PORT), Handler)
    # terminate with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)


