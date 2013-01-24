#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import Int8
import threading
import listener_thread as lthread
import time

data = None
initialTime = time.time()

def printMessage():
    while True:
        currentTime = time.time()
        if(currentTime - initialTime == 500):
            print "Hello I'm running...\n"
            data = lthread.getData()
            if(data <> None):
                print "Data is %s" % data

if __name__ == '__main__':
    try:
        print "Running the main program...\n"
        #initialTime = time.time()
        thread1 = lthread.listenerThread("listenerThread", "commands")
        thread2 = threading.Thread(target = printMessage)
        print "2 threads created...\n"
        print "Thread 1 started...\n"
        thread1.start()
        print "Thread 2 started...\n"
        thread2.start()
        threadList = []
        threadList.append(thread1)
        threadList.append(thread2)
        for t in threadList:
            t.join()
            print "1 thread joined"
    except KeyboardInterrupt:
        sys.exit(0)
