import roslib; roslib.load_manifest('tf_test')
import rospy
import tf

BR = None
RATE = None

def init_broadcaster():
    rospy.init_node('test_broadcaster')
    BR = tf.TransformBroadcaster()
    RATE = rospy.rate(10)

if __name__ == '__main__':
    init_broadcaster()
    try:
        while not rospy.is_shutdown():
            BR.sendTransform((1.0, 1.0, 1.0),
                            tf.transformations.quaternion_from_euler(0, 0, 1),
                            rospy.Time.now(),
                            "child",
                            "parent")
            RATE.sleep()
    except KeyboardInterrupt:
        sys.exit(0)
