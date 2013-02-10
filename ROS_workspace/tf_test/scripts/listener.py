import roslib; roslib.manifest('tf_test')
import rospy
import tf

LS = None

def init_listener():
    rospy.init_node('test_listener')
    LS = tf.tf.TransformListener()
    
if __name__ == '__main__':
    init_listener()
    try:
        while not rospy.is_shutdown():
            now = rospy.Time.now() - rospy.Duration(5.0)
            LS.waitForTransformation('child', 'parent', now, rospy.Duration(10.0))
            (trans, rot) = LS.lookupTransform('child', 'parent', now)
            print 'find something' + trans + rot
    except KeyboardInterrupt:
        sys.exit(0)