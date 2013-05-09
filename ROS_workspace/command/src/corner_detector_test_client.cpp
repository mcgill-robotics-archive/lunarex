#include "ros/ros.h"
#include "corner_detector/corner_detector.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "corner_detector_test_client");

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<corner_detector::corner_detector>("corner_detector");
  corner_detector::corner_detector srv;
  srv.request.map = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);
  if (client.call(srv))
  {
    ROS_INFO("Sum: %ld", (long int)srv.response.sum);
  }
  else
  {
    ROS_ERROR("Failed to call service add_two_ints");
    return 1;
  }

  return 0;
}

