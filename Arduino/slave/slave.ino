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
// Defines used for the IMU:
//=====================================================================
#define GRAVITY 256  //this equivalent to 1G in the raw data coming from the accelerometer 
#define ToRad(x) ((x)*0.01745329252)  // *pi/180
#define ToDeg(x) ((x)*57.2957795131)  // *180/pi
// L3G4200D gyro: 2000 dps full scale
// 70 mdps/digit; 1 dps = 0.07
#define Gyro_Gain_X 0.07
#define Gyro_Gain_Y 0.07
#define Gyro_Gain_Z 0.07
#define Gyro_Scaled_X(x) ((x)*ToRad(Gyro_Gain_X))
#define Gyro_Scaled_Y(x) ((x)*ToRad(Gyro_Gain_Y))
#define Gyro_Scaled_Z(x) ((x)*ToRad(Gyro_Gain_Z))
#define Kp_ROLLPITCH 0.02
#define Ki_ROLLPITCH 0.00002
#define Kp_YAW 1.2
#define Ki_YAW 0.00002
// Used to calibrate the magnetometer:
#define M_X_MIN -150
#define M_Y_MIN -150
#define M_Z_MIN -150
#define M_X_MAX 150
#define M_Y_MAX 150
#define M_Z_MAX 150

//=====================================================================
// Variables used for the IMU:
//=====================================================================
int SENSOR_SIGN[9] = {1,-1,-1,-1,1,1,1,-1,-1};
float G_Dt=0.02;    // Integration time (DCM algorithm)  We will run the integration loop at 50Hz if possible
long imuTimer=0;   //general purpuse timer
long imuTimerOld;
int AN[6]; //array that stores the gyro and accelerometer data
int AN_OFFSET[6]={0,0,0,0,0,0}; //Array that stores the Offset of the sensors
int gyro_x;
int gyro_y;
int gyro_z;
int accel_x;
int accel_y;
int accel_z;
int magnetom_x;
int magnetom_y;
int magnetom_z;
float c_magnetom_x;
float c_magnetom_y;
float c_magnetom_z;
float MAG_Heading;
float Accel_Vector[3]= {0,0,0};
float Gyro_Vector[3]= {0,0,0};
float Omega_Vector[3]= {0,0,0};
float Omega_P[3]= {0,0,0};
float Omega_I[3]= {0,0,0};
float Omega[3]= {0,0,0};
float errorRollPitch[3]= {0,0,0}; 
float errorYaw[3]= {0,0,0};
unsigned int counter=0;
byte gyro_sat=0;
float DCM_Matrix[3][3]= { {1,0,0}, {0,1,0}, {0,0,1} }; 
float Update_Matrix[3][3]={{0,1,2},{3,4,5},{6,7,8}}; //Gyros here
float Temporary_Matrix[3][3]={ {0,0,0}, {0,0,0}, {0,0,0} };

// Euler angles
float roll;
float pitch;
float yaw;

boolean activeIMU = false;
boolean printData = false;

//=====================================================================
// Variables used for ROS
//=====================================================================

ros::Nodehandle nh;
std_msgs::Float32 sendHeading;
std_msgs::Float32 bestHeading;
std_msgs::String str_msg;

// Publishers:
ros::Publisher chatter("chatter", &str_msg);
ros::Publisher pub_IMU("heading", &sendHeading);

// Subscriber:
ros::Subscriber<std_msgs::Int8> sub_IMU("reset", &resetIMU);
roS::Subscriber<stf_msgs::Float32> sub_bestHeading("bestHeading", );

void setup() {
  nh.initNode();
  
  // Advertise publishers:
  nh.advertise(chatter);
  nh.advertise(pub_IMU);
  
  // Subscribe subscribers:
  nh.subscribe(sub_IMU);
}

void loop() {
  nh.spinOnce();
  
  if (activeIMU) {
    updateIMU();
  }
}
