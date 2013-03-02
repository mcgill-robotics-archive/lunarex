#!/usr/bin/env python
import roslib
roslib.load_manifest('tf_service_test')
import rospy
import math
import tf
from tf.transformations import euler_from_quaternion

if __name__ == '__main__':
    rospy.init_node('tf_listen')
    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('W', 'A', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException):
            print 'Error!'
            continue

        #print 'translation: ',trans
        angles = euler_from_quaternion(rot)
        print 'rotation: ',[(180.0/math.pi)*i for i in angles]

        rate.sleep()
