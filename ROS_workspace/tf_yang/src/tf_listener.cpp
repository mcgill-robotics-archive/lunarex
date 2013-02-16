/****************************************************************/
/**the purpose of this node is to transform the local origin*****/
/**position from the sensor position to the robot center    *****/
/**Input: No                                                *****/
/**Output: geometry_msgs::pos                               *****/
/****************************************************************/

#include <ros/ros.h>
#include <geometry_msgs/PointStamped.h>
#include <tf/transform_listener.h>

//TODO: Measure the required dimensions
static const float_t tf_loc_position_x = 0; // since the set of sensor is always put right in front of the robot, let assume its locol position is zero
static const float_t tf_loc_position_y = 0; 
static const float_t tf_loc_position_z = 0; // the height of sensors has to be measured

void transformPoint(const tf::TransformListener& listener){
    //we'll create a point in the base_laser frame that we'd like to transform to the base_link frame
    geometry_msgs::PointStamped laser_point;
    laser_point.header.frame_id = "base_laser";


    //we'll just use the most recent transform available for our simple example
    laser_point.header.stamp = ros::Time();

    laser_point.point.x = tf_loc_position_x;
    laser_point.point.y = tf_loc_position_y;
    laser_point.point.z = tf_loc_position_z;

    try{
        geometry_msgs::PointStamped base_point;
        listener.transformPoint("base_link", laser_point, base_point);

    }
    catch(tf::TransformException& ex){
        ROS_ERROR("Received an exception trying to transform a point from \"base_laser\" to \"base_link\": %s", ex.what());
    }
}

int main(int argc, char** argv){
    ros::init(argc, argv, "robot_tf_listener");
    ros::NodeHandle n;

    tf::TransformListener listener(ros::Duration(10));

    //we'll transform a point once every second
    ros::Timer timer = n.createTimer(ros::Duration(1.0), boost::bind(&transformPoint, boost::ref(listener)));

    ros::spin();

}
