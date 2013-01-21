#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import Int8
import threading

class serverListerner:

    def callback(data):
        rospy.loginfo(rospy.get_name() + ": I heard %s" % data.data)
        
    def initlistener(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("commands", Int8, self.callback)
    
    def printlistener(self):
        print "Yes?"


if __name__ == '__main__':
    try:
        listener = new serverListener()
        listener.initlistener()
        thread_1 = threading.Thread(target = rospy.spin())
        thread_2 = threading.Thread(target = listener.printlistener())
        thread_1.start()
        thread_1.join()
        thread_2.start()
        thread_2.join()
    except KeyboardInterrupt:
        sys.exit(0)
