#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import Int8
import threading
import time

thread_data = 0
pub = None
NODE_NAME = "Listener_Multithread"

def callback(data):
    thread_data = data.data
    print "I heard %s" % thread_data

class listenerThread(threading.Thread):
    def __init__(self):
        print "Initiating thread...\n"
        #rospy.Subscriber(topic, Int8, callback)
        print "ROS subscriber initiated...\n"
        threading.Thread.__init__(self)

    def run(self):
        try:
            print "Currently running ROS subscriber thread...\n"
            rospy.spin()
        except KeyboardInterrupt:
            sys.exit(0)

class publisherThread(threading.Thread):
    def __init__(self):
        print "Initiating publisher thread...\n"
        #pub = rospy.Publisher('listen_pub', Int8)
        #rospy.init_node('listenerThread_pub')
        print "ROS publisher initiated...\n"
        threading.Thread.__init__(self)

    def run(self):
        try:
            #while not rospy.is_shutdown():
            print "Proof that the publisher thread is running...\n"
            while True:
                #print "Proof that publisher is running...\n"
                if(thread_data <> 0):
                    print "Data: %s" % thread_data
                    pub.publish(thread_data)
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
        rospy.init_node(NODE_NAME)
        pub = rospy.Publisher("listenpub", Int8)
        pub.publish(20)         #Test publisher
        rospy.Subscriber("commands", Int8, callback)
        #initialTime = time.time()
        pub.publish(20)         #Test publisher
        thread1 = listenerThread()
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
