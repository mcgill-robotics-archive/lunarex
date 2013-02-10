#!/usr/bin/env python
import roslib; roslib.load_manifest('tf_test')
import rospy
import tf
import sys


if __name__ == '__main__':
    rospy.init_node('test_listener')
    LS = tf.TransformListener()
    try:
        while not rospy.is_shutdown():
            now = rospy.Time.now()
            #LS.waitForTransform('child', 'parent', now, rospy.Duration(10.0))
            (trans, rot) = LS.lookupTransform('child', 'parent', now)
            print 'find something' + trans + rot
    except KeyboardInterrupt:
        sys.exit(0)
