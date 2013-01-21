#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import Int8
import threading

def callback(data):
    rospy.loginfo(rospy.get_name() + ": I heard %s" % data.data)

def printSomething(str):
    print "Can you see this line?\n"

if __name__ == '__main__':
    try:
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("commands", Int8, callback)
        thread_1 = threading.Thread(target = rospy.spin())
        thread_2 = threading.Thread(target = printSomething('hello'))
        thread_1.start()
        thread_2.start()
        thread_1.join()
        thread_2.join()
    except KeyboardInterrupt:
        sys.exit(0)
