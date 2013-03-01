/*=====================================================================
//  Name: slave
//
//  Authors:
//    Jean-Sébastien Déry
//
//  Purpose:
//    This is to receive/send information from/to the laptop.
//===================================================================*/

//=====================================================================
// Includes:
//=====================================================================
#include <ros.h>
#include <std_msgs/Int8.h>
#include <std_msgs/String.h>
#include <PID_v1.h>
#include <Wire.h>

//=====================================================================
// Constants used for the confirmation sent to the laptop:
//=====================================================================
const char OK_CONNECTION[14] = "OK CONNECTION";
const char OK_IMU_RESET[13] = "OK IMU RESET";
const char OK_SUSP_HIGH[13] = "OK SUSP HIGH";
const char OK_SUSP_LOW[12] = "OK SUSP LOW";
const char OK_DOOR_OPEN[13] = "OK DOOR OPEN";
const char OK_DOOR_CLOSED[15] = "OK DOOR CLOSED";

//=====================================================================
// Variables used by the IMU that need to be global:
//=====================================================================
int SENSOR_SIGN[9] = {1,-1,-1,-1,1,1,1,-1,-1};
int AN_OFFSET[6]={0,0,0,0,0,0}; //Array that stores the Offset of the sensors
int AN[6]; //array that stores the gyro and accelerometer data
int gyro_x;
int gyro_y;
int gyro_z;
int accel_x;
int accel_y;
int accel_z;
int magnetom_x;
int magnetom_y;
int magnetom_z;
boolean activeIMU = false;
boolean printData = false;

//=====================================================================
// Variables used by ROSSERIAL:
//=====================================================================

/*ros::Nodehandle nh;
std_msgs::Float32 sendHeading;
std_msgs::Float32 bestHeading;
std_msgs::String str_msg;

// Publishers:
ros::Publisher chatter("chatter", &str_msg);
ros::Publisher pub_IMU("heading", &sendHeading);

// Subscriber:
ros::Subscriber<std_msgs::Int8> sub_IMU("reset", &resetIMU);
roS::Subscriber<stf_msgs::Float32> sub_bestHeading("bestHeading", );*/

void setup() {
  /*nh.initNode();
  
  // Advertise publishers:
  nh.advertise(chatter);
  nh.advertise(pub_IMU);
  
  // Subscribe subscribers:
  nh.subscribe(sub_IMU);*/
}

void loop() {
  //nh.spinOnce();
  
  if (activeIMU) {
    updateIMU();
  }
}
