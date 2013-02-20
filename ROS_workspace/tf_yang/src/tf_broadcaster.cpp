#include <ros/ros.h>
#include <tf/transform_broadcaster.h>.h>

/* Define the difference between the locations of major sensor and the acutal robot center point on 3-D space */
static const float_t    tf_coordianate_diff_x = 0.77;
static const float_t    tf_coordianate_diff_y = 0.0;        // it is zero most of time
static const float_t    tf_coordianate_diff_z = 0.0;        // it will be figured out, but let us assume it as zero right now
static const uint16_t   tf_Env_Rate = 50;                  // make the loop work every 50 Hz per turn


int main(int argc, char** argv){
    ros::init(argc, argv, "robot_tf_publisher");
    ros::NodeHandle n;

    ros::Rate r( tf_Env_Rate );

    tf::TransformBroadcaster broadcaster;

    while(n.ok()){
        broadcaster.sendTransform(
            tf::StampedTransform(
                tf::Transform(tf::Quaternion(0, 0, 0, 1), 
                tf::Vector3(tf_coordianate_diff_x , tf_coordianate_diff_y, tf_coordianate_diff_z)),
                ros::Time::now(),"base_footprint", "base_laser"));
        r.sleep();
    }
}
