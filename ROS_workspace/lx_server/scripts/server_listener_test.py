#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import Int8
import threading
import time

thread_data = None
pub = None
NODE_NAME = "Listener_Multithread"

def callback(data):
    thread_data = data.data
    print "I heard %s" % thread_data

class listenerThread(threading.Thread):
    def __init__(self, NODE_NAME, topic):
        print "Initiating thread...\n"
        self.NODE_NAME = NODE_NAME
        self.topic = topic
        rospy.Subscriber(self.topic, Int8, callback)
        print "ROS subscriber initiated...\n"
        threading.Thread.__init__(self)

    def run(self):
        try:
            print "Currently running ROS subscriber thread...\n"
            rospy.spin()
        except KeyboardInterrupt:

class publisherThread(threading.Thread):
    def __init__(self):
        print "Initiating publisher thread...\n"
        pub = rospy.Publisher('listen_pub', Int8)
        #rospy.init_node('listenerThread_pub')
        self.thread_data = None
        print "ROS publisher initiated...\n"
        threading.Thread.__init__(self)

    def run(self):
        try:
            while not rospy.is_shutdown():
                if(thread_data <> None):
                    pub.publish(self.thread_data)
                    rospy.sleep(1.0)
                
        except KeyboardInterrupt:
            sys.exit(0)

'''
def printMessage():
    while True:
        currentTime = time.time()
        if(currentTime - initialTime == 500):
            print "Hello I'm running...\n"
            data = lthread.getData()
            if(data <> None):
                print "Data is %s" % data
'''

if __name__ == '__main__':
    try:
        print "Running the main program...\n"
        rospy.init_node(NODE_NAME, anonymous = True)
        #initialTime = time.time()
        thread1 = listenerThread("listenerThread", "commands")
        #thread2 = threading.Thread(target = printMessage)
        thread2 = publisherThread()
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
