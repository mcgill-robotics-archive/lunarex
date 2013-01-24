#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import Int8
import threading
import lister_thread as lthread

data = None

def printMessage():
    data = lthread.getData()
    if(data <> None):
        print "Data is %s" % data

if __name__ == '__main__':
    try:
        thread1 = lthread.listenerThread("listenerThread", "commands")
        thread2 = threading.Thread(target = printMessage)
        thread1.start()
        thread2.start()
        threadList = []
        threadList.append(thread1)
        threadList.append(thread2)
        for t in threadList:
            t.join()
    except KeyboardInterrupt:
        sys.exit(0)