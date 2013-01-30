#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import Int8

class subpub:
    def __init__(self):
        self.data = 0
        rospy.init_node("pubsub")

        self.pub = rospy.Publisher('Pubsub', Int8, latch = True)
        rospy.Subscriber("commands", Int8, self.callback)

    def callback(self, data):
        self.data = data.data

    def run(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.pub.publish(self.data)
            rate.sleep()


if __name__ == '__main__':
    try:
        test = subpub()
        test.run()
    except KeyboardInterrupt:
        sys.exit(0)
