#!/usr/bin/env python
import roslib; roslib.load_manifest('tf_test')
import rospy
import tf
import sys


if __name__ == '__main__':
    rospy.init_node('test_broadcaster')
    BR = tf.TransformBroadcaster()
    RATE = rospy.Rate(10.0)
    try:
        while not rospy.is_shutdown():
            BR.sendTransform((1.0, 1.0, 1.0),
                            (0.0, 0.0, 0.0, 1.0),
                            rospy.Time.now(),
                            "child",
                            "parent")
            print 'Sended 1'
            RATE.sleep()
        print 'Out of the loop'
    except KeyboardInterrupt:
        sys.exit(0)
