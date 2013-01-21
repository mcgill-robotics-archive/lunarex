#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import Int8
import threading

def callback(data):
    rospy.loginfo(rospy.get_name() + ": I heard %s" % data.data)

class serverListener:

    def __init__(self):
        rospy.init_node('listener', anonymous = True)
        rospy.Subscriber("commands", Int8, callback)

    def printlistener(self):
        print "Yes?\n"


if __name__ == '__main__':
    try:
        listener = serverListener()
        thread_1 = threading.Thread(target = rospy.spin())
        thread_2 = threading.Thread(target = listener.printlistener())
        thread_1.start()
        thread_1.join()
        thread_2.start()
        thread_2.join()
    except KeyboardInterrupt:
        sys.exit(0)
