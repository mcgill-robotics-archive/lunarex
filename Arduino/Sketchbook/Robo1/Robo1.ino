#include <Servo.h>
#include <ros.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Bool.h>
#include <std_msgs/UInt8.h>
#include <geometry_msgs/Twist.h>

//#include <arduino_msgs/ArduinoFeedback.h>
        
/* ========== ROS stuff ================

Order of Operations: (what's going to happen in the ROS section of code)

1. define nodehandle - rose node object 
2. Initialize arduino variables that will be set in ROS
3. define arduino callback functions that set arduino variables
4. subscribe to topics (point to arduino callback functions)
5. create publishers for feedback
6. nh.initNode() and subscribe to subscribers and advertise publishers in Setup()
7. nh.spinOnce() at the end of loop()
8. use arduino variables within functions
*/

ros:: NodeHandle nh;

//Init Values for all variables set by ROS topics

//Convention: use smallBig for arduino variable, under_score for ros topic
float angSpeed = 0;
float linSpeed = 0;
float dumpPos = 255; //down as default
float suspPos = 0; //up as default
float doorPos = 0; //closed by default
float augerSpeed = 0;

//Subscriber callback functions
//Convention: use smallBig for arduino variable, under_score for ros topic

void setSpeeds(const geometry_msgs::Twist &cmd_vel){
  linSpeed = (float) cmd_vel.linear.x;
  angSpeed = (float) cmd_vel.angular.z;
}
void setDumpLA(const std_msgs::UInt8 &dump_pos){
  dumpPos = (int) dump_pos.data;
}
void setSuspLA(const std_msgs::UInt8 &susp_pos){
  suspPos = (int) susp_pos.data;
}  
void setDoorLA(const std_msgs::UInt8 &door_pos){
   doorPos= (int) door_pos.data;
}
void setAugerSpeed(const std_msgs::UInt8 &auger_speed){
  augerSpeed = (int) auger_speed.data;
}

//Subsribers: instantiate subscribers and specify callback functions
// Format: ros:: Subsriber<message type> subscriberName("topic", &callbackFunction);
ros:: Subscriber<geometry_msgs::Twist> cmdVelSub("cmd_vel", &setSpeeds);  
ros:: Subscriber<std_msgs::UInt8> dumpLASub("dump_pos", &setDumpLA); //dumping Linear Acutator position
ros:: Subscriber<std_msgs::UInt8> suspLASub("susp_pos", &setSuspLA); //suspension Linear Actuator position (same for both)
ros:: Subscriber<std_msgs::UInt8> doorLASub("door_pos", &setDoorLA); //door Linear Acutator position (same for both)
ros:: Subscriber<std_msgs::UInt8> augerSpeedSub("auger_speed", &setAugerSpeed); //auger motor speed

//Publishers

//repeat 2 lines below for each publisher
//std_msgs::Float32 fb_angspeed;
//ros:: Publisher fb_angspeed_publisher("fb_angspeed", &fb_angspeed);

//arduino_msgs::ArduinoFeedback fb;
//ros:: Publisher feedback_publisher("arduino_feedback", &fb);

// =========== Pin mappings ==============

Servo LF_servo, RF_servo, LR_servo, RR_servo;
Servo augerSudoServo;


int SUSP_ACTUATOR_PIN = 6;
int DUMP_ACTUATOR_PIN = 7;
int AUGER_MOTOR_PIN = 8;
int DOOR_ACTUATOR_PIN = 13;

int LF_SERVO_PIN = 2;
int RF_SERVO_PIN =3;
int LR_SERVO_PIN = 4;
int RR_SERVO_PIN = 5;

//the following 12 pins verified May 10 for the second time, due to crappy gitub
int LF_motor_dir_pin = 32;
int RF_motor_dir_pin = 30;
int LR_motor_dir_pin = 28;
int RR_motor_dir_pin = 26;

int LF_motor_enable_pin = 33;
int RF_motor_enable_pin = 31;
int LR_motor_enable_pin = 29;
int RR_motor_enable_pin = 27;

int LF_motor_pin = 12;
int RF_motor_pin = 11;
int LR_motor_pin = 10;
int RR_motor_pin = 9;

//-----------Variables used to set motor speeds/enable/directions

//disable drive motors by default
boolean LF_motor_enable = 0;
boolean RF_motor_enable = 0;
boolean LR_motor_enable = 0;
boolean RR_motor_enable = 0;

boolean LF_motor_dir = 0;  
boolean RF_motor_dir = 0;
boolean LR_motor_dir = 0;
boolean RR_motor_dir = 0;

float LF_wheel_rpm = 0.0;
float RF_wheel_rpm = 0.0;
float LR_wheel_rpm = 0.0;
float RR_wheel_rpm = 0.0;

//SET STRAIGHT AS DEFAULT
float LF_servo_angle = 90.0;
float RF_servo_angle = 90.0;
float LR_servo_angle = 90.0;
float RR_servo_angle = 90.0;

int LF_servo_cmd = 0;
int RF_servo_cmd = 0;
int LR_servo_cmd = 0;
int RR_servo_cmd = 0;

int LF_motor_cmd = 0;
int RF_motor_cmd = 0;
int LR_motor_cmd = 0;
int RR_motor_cmd = 0;


//-----------------CONSTANTS

float WHEEL_RADIUS = 0.1397;
float MIN_SPEED = 0;
float MAX_SPEED = 20000; // in RPM
float LENGTH = 0.8;   //.6858 is 27 inches   -measured .8 when up
float WIDTH = 0.7219;    //.6604 is 26 inches -measured .73 when up
float DIST_TO_AXIS_A = 0.5074;

int SEC_PER_MIN = 60;
int GEAR_RATIO = 74;

float TOL = 0.5;
float ANG_STOP_THRESH = 0.05;    //any angular speed less than this will be interpreted as zero
float LIN_STOP_THRESH = 0.05;    //any linear speed less than this will be interpreted as zero

int SUSP_INTERFERENCE_LIMIT = 50; //command sent to suspension actuators. values greater than this correspond to mining (0 travel, 255 full mine)
float MINING_MAX_SERVO_ANGLE_FRONT = 0;
float MINING_MAX_SERVO_ANGLE_REAR = 40;
float TRAVEL_MAX_SERVO_ANGLE_FRONT = 80;
float TRAVEL_MAX_SERVO_ANGLE_REAR = 80;

int WATCHDOG_TIMEOUT = 15; //reset linspeed+angspeed to zero after at least this many seconds  (max number to choose here is about 45-50 seconds)






void setup()
{
  //prep for linearActuator Signals PWM
  pinMode(SUSP_ACTUATOR_PIN, OUTPUT);
  pinMode(DUMP_ACTUATOR_PIN, OUTPUT);
  pinMode(DOOR_ACTUATOR_PIN, OUTPUT);
  
  // ===== Driving and Steering ====
  pinMode(LF_motor_pin, OUTPUT);
  pinMode(RF_motor_pin, OUTPUT);
  pinMode(LR_motor_pin, OUTPUT);
  pinMode(RR_motor_pin, OUTPUT);

  LF_servo.attach(LF_SERVO_PIN);
  RF_servo.attach(RF_SERVO_PIN);
  LR_servo.attach(LR_SERVO_PIN);
  RR_servo.attach(RR_SERVO_PIN);
  
  augerSudoServo.attach(AUGER_MOTOR_PIN);
  
  pinMode(LF_motor_enable_pin, OUTPUT);
  pinMode(RF_motor_enable_pin, OUTPUT);
  pinMode(LR_motor_enable_pin, OUTPUT);
  pinMode(RR_motor_enable_pin, OUTPUT);

  pinMode(LF_motor_dir_pin, OUTPUT);
  pinMode(RF_motor_dir_pin, OUTPUT);
  pinMode(LR_motor_dir_pin, OUTPUT);
  pinMode(RR_motor_dir_pin, OUTPUT);
  
  nh.initNode();
  nh.subscribe(cmdVelSub);
  nh.subscribe(dumpLASub);
  nh.subscribe(suspLASub);
  nh.subscribe(doorLASub);
  nh.subscribe(augerSpeedSub);  
 // nh.advertise(fb_angspeed_publisher);
}









unsigned int count = 0;  //count loops for timeout
void loop()
{
  
  // ===== Driving and Steering ======
  if (abs(linSpeed) <= LIN_STOP_THRESH && abs(angSpeed) <= ANG_STOP_THRESH)    //No linear; No Angular
    {stopAll();}
  else if(abs(linSpeed) <= LIN_STOP_THRESH)    //Angular but no linear
    {
    if (suspPos < SUSP_INTERFERENCE_LIMIT) // only in travelling mode
      {
        turnOnSpot();
      }
    }
  else if(abs(angSpeed) <= ANG_STOP_THRESH)   //Linear but no angular
    {goStraight();}
  else                  //general combo of linear and angular
  {
    if (suspPos > SUSP_INTERFERENCE_LIMIT)
    {
      miningAckerman();
    }
    else
    {  
      doAckerman();
    }
  }
  
  
  
  

  
  //push commmands to motors:
  setWheelAngle();  
  setWheelDirection();
  setWheelSpeed();
  applyMotorEnable();
  
  
  // ===== Actuators and Auger ======
  
  // Send signal between [0,255] to actuators:
  analogWrite(SUSP_ACTUATOR_PIN, suspPos); 
  analogWrite(DUMP_ACTUATOR_PIN, dumpPos);
  analogWrite(DOOR_ACTUATOR_PIN, doorPos);
  
  int augerSignal = map(augerSpeed, 0, 255, 1000, 2000);
  augerSudoServo.writeMicroseconds(augerSignal);    //analogWrite() didnt work for burnt motor controller, May 13 Nick

  
  // ===== PUBLISH FEEDBACK HERE ??  =====
  
  //populateFeedbackMessage();
  // fb_angspeed.data=angSpeed;
  // fb_angspeed_publisher.publish(&fb_angspeed);

  nh.spinOnce();

  count += 1;
  if (count >= WATCHDOG_TIMEOUT*1333)  //unsigned int goes up to 65,535  //approximately 1333 loops per second
  {
    count = 0;
  }
  
  if (count == 0)  //unsigned int goes up to 65,535  //approximately 1300 loops per second
  {
    angSpeed = 0;
    linSpeed = 0;
  }
    

}

void stopAll()
{
  LF_wheel_rpm = 0.0;
  RF_wheel_rpm = 0.0;
  LR_wheel_rpm = 0.0;
  RR_wheel_rpm = 0.0;
  
  LF_motor_enable = 0;
  RF_motor_enable = 0; 
  LR_motor_enable = 0;
  RR_motor_enable = 0;
}

void turnOnSpot()
{
  LF_motor_enable = 1;
  RF_motor_enable = 1;
  LR_motor_enable = 1;
  RR_motor_enable = 1;
  
  LF_servo_angle = 135;
  RF_servo_angle = 45;
  LR_servo_angle = 45;
  RR_servo_angle = 135;
   
  if(angSpeed>0){   
     //we assume here that 1 = forward, 0 = backward
     LF_motor_dir = 0;
     RF_motor_dir = 1;
     LR_motor_dir = 0;
     RR_motor_dir = 1;
   }
   else if(angSpeed < 0){
     LF_motor_dir = 1;
     RF_motor_dir = 0;
     LR_motor_dir = 1;
     RR_motor_dir = 0;
   }
   
   float all_four_motor_rpms = (DIST_TO_AXIS_A / WHEEL_RADIUS)*abs(angSpeed)*SEC_PER_MIN/(2.0*PI);
   
   LF_wheel_rpm = all_four_motor_rpms;
   RF_wheel_rpm = all_four_motor_rpms;
   LR_wheel_rpm = all_four_motor_rpms;
   RR_wheel_rpm = all_four_motor_rpms;    
}




void goStraight()
{

  LF_motor_enable = 1;
  RF_motor_enable = 1;
  LR_motor_enable = 1;
  RR_motor_enable = 1;
  
  LF_servo_angle = 90.0;
  RF_servo_angle = 90.0;
  LR_servo_angle = 90.0;
  RR_servo_angle = 90.0;
    
  if(linSpeed>0)
  {
    LF_motor_dir = 1;
    RF_motor_dir = 1;
    LR_motor_dir = 1;
    RR_motor_dir = 1;
  }
  else if(linSpeed < 0)
  {
    LF_motor_dir = 0;
    RF_motor_dir = 0;
    LR_motor_dir = 0;
    RR_motor_dir = 0;
  }
  
  float all_four_motor_rpms = SEC_PER_MIN*abs(linSpeed)/(2.0*PI*WHEEL_RADIUS);
  
  LF_wheel_rpm = all_four_motor_rpms;
  RF_wheel_rpm = all_four_motor_rpms;
  LR_wheel_rpm = all_four_motor_rpms;
  RR_wheel_rpm = all_four_motor_rpms;  
}







void doAckerman()
{ 
  LF_motor_enable = 1;
  RF_motor_enable = 1;
  LR_motor_enable = 1;
  RR_motor_enable = 1;
 
 if(linSpeed < 0) 
  {
    LF_motor_dir = 0;
    RF_motor_dir = 0;
    LR_motor_dir = 0;
    RR_motor_dir = 0;
  }
  
  else if(linSpeed > 0)
  {
    LF_motor_dir = 1;
    RF_motor_dir = 1;
    LR_motor_dir = 1;
    RR_motor_dir = 1;
  }


  //Ackerman steering is characterised by setting wheel angles and speeds. Do general computations first:  
  angSpeed = constrain(angSpeed, -2*linSpeed, 2*linSpeed);
  float ackRadius = abs(linSpeed/angSpeed);    
  //Angle  
  float innerAngle = atan((LENGTH/2.0)/(ackRadius - (WIDTH/2.0)))*180.0/PI;  //servo angle for both wheels on the inside of the turn
  float outerAngle = atan((LENGTH/2.0)/(ackRadius + (WIDTH/2.0)))*180.0/PI; 
  //Speed
  float innerRadius = sqrt(pow(LENGTH/2.0, 2) + pow(ackRadius - WIDTH/2.0, 2));  //distance from inner wheels to center of rotation
  float outerRadius = sqrt(pow(LENGTH/2.0, 2) + pow(ackRadius + WIDTH/2.0, 2));
  float innerRPM = (innerRadius / WHEEL_RADIUS) * abs(angSpeed)*SEC_PER_MIN/(2.0*PI); //speed of inner wheels
  float outerRPM = (outerRadius / WHEEL_RADIUS) * abs(angSpeed)*SEC_PER_MIN/(2.0*PI);

  // There are 4 permutations of linSpeed and angSpeed, with each corresponding to one of two cases: an instantaneously circular trajectory about a point to the left or right of the robot
  
  float trajectoryCenterLocation = (angSpeed * linSpeed);  //Point on left if positive, point on right if negative   --   Magnitude is meaningless
  
  if (trajectoryCenterLocation > 0.0)
  {
    // center of rotation is on left: CCW+Forwards or CW+Backwards
    
    LF_servo_angle = 90 - innerAngle;
    RF_servo_angle = 90 - outerAngle;
    LR_servo_angle = 90 + innerAngle;
    RR_servo_angle = 90 + outerAngle;
    
    LF_wheel_rpm = innerRPM;
    RF_wheel_rpm = outerRPM;
    LR_wheel_rpm = innerRPM;
    RR_wheel_rpm = outerRPM;
   
  }
  else
  {
    // center of rotation is on Right: CW+Forwards or CCW+Backwards
    LF_servo_angle = 90.0 + outerAngle;
    RF_servo_angle = 90.0 + innerAngle;
    LR_servo_angle = 90.0 - outerAngle;
    RR_servo_angle = 90.0 - innerAngle;
    
    LF_wheel_rpm = outerRPM;
    RF_wheel_rpm = innerRPM;
    LR_wheel_rpm = outerRPM;
    RR_wheel_rpm = innerRPM;
  }
}
  
void miningAckerman()  
{ 
  LF_motor_enable = 1;
  RF_motor_enable = 1;
  LR_motor_enable = 1;
  RR_motor_enable = 1;
 
 if(linSpeed < 0) 
  {
    LF_motor_dir = 0;
    RF_motor_dir = 0;
    LR_motor_dir = 0;
    RR_motor_dir = 0;
  }
  
  else if(linSpeed > 0)
  {
    LF_motor_dir = 1;
    RF_motor_dir = 1;
    LR_motor_dir = 1;
    RR_motor_dir = 1;
  }
  //scale for slow mining
  
  angSpeed = constrain(angSpeed, -2*linSpeed, 2*linSpeed);  //ackerman radius always greater than 0.5
  
  //Ackerman steering is characterised by setting wheel angles and speeds. Do general computations first:  
  float ackRadius = abs(linSpeed/angSpeed);    
  //Angle  
  float innerAngle = atan(LENGTH/(ackRadius - (WIDTH/2.0)))*180.0/PI;  //servo angle for both wheels on the inside of the turn
  float outerAngle = atan(LENGTH/(ackRadius + (WIDTH/2.0)))*180.0/PI; 
  // front wheels straight ahead at 90
  
  //Speed
  float innerBackRadius = sqrt(pow(LENGTH, 2) + pow(ackRadius - WIDTH/2.0, 2));  //distance from inner wheels to center of rotation
  float outerBackRadius = sqrt(pow(LENGTH, 2) + pow(ackRadius + WIDTH/2.0, 2));
  float innerFrontRadius = ackRadius - WIDTH/2.0;  //distance from inner wheels to center of rotation
  float outerFrontRadius = ackRadius + WIDTH/2.0;
  
  float innerBackRPM = (innerBackRadius / WHEEL_RADIUS) * abs(angSpeed)*SEC_PER_MIN/(2.0*PI); //speed of inner wheels
  float outerBackRPM = (outerBackRadius / WHEEL_RADIUS) * abs(angSpeed)*SEC_PER_MIN/(2.0*PI);
  float innerFrontRPM = (innerFrontRadius / WHEEL_RADIUS) * abs(angSpeed)*SEC_PER_MIN/(2.0*PI); //speed of inner wheels
  float outerFrontRPM = (outerFrontRadius / WHEEL_RADIUS) * abs(angSpeed)*SEC_PER_MIN/(2.0*PI);

  // There are 4 permutations of linSpeed and angSpeed, with each corresponding to one of two cases: an instantaneously circular trajectory about a point to the left or right of the robot
  float trajectoryCenterLocation = (angSpeed * linSpeed);  //Point on left if positive, point on right if negative   --   Magnitude is meaningless
  
  if (trajectoryCenterLocation > 0.0)
  {
    // center of rotation is on left: CCW+Forwards or CW+Backwards
    
    LF_servo_angle = 0;
    RF_servo_angle = 0;
    LR_servo_angle = 90 + innerAngle;
    RR_servo_angle = 90 + outerAngle;
    
    LF_wheel_rpm = innerFrontRPM;
    RF_wheel_rpm = outerFrontRPM;
    LR_wheel_rpm = innerBackRPM;
    RR_wheel_rpm = outerBackRPM;
   
  }
  else
  {
    // center of rotation is on Right: CW+Forwards or CCW+Backwards
    LF_servo_angle = 90.0;
    RF_servo_angle = 90.0;
    LR_servo_angle = 90.0 - outerAngle;
    RR_servo_angle = 90.0 - innerAngle;
    
    LF_wheel_rpm = outerFrontRPM;
    RF_wheel_rpm = innerFrontRPM;
    LR_wheel_rpm = outerBackRPM;
    RR_wheel_rpm = innerBackRPM;
  }
}

void setWheelDirection()
{
  //Account for the fact that the motors on the right are mounted in the opposite orientation:
  RF_motor_dir = !RF_motor_dir;
  RR_motor_dir = !RR_motor_dir;
  
  //forward or backwards for drive wheels
  digitalWrite(LF_motor_dir_pin, LF_motor_dir);
  digitalWrite(RF_motor_dir_pin, RF_motor_dir);
  digitalWrite(LR_motor_dir_pin, LR_motor_dir);
  digitalWrite(RR_motor_dir_pin, RR_motor_dir);
}

void setWheelAngle()
{ 
  // pushes values to motors
  
  //initialize limits on what commands can be sent
  //define the variables
  int frontServoLowerLimit_cmd = 1000;
  int frontServoUpperLimit_cmd = 2000;
  int rearServoLowerLimit_cmd = 1000;
  int rearServoUpperLimit_cmd = 2000;
  
  //convert angle in degrees to command
  LF_servo_cmd = map(LF_servo_angle,0,180,1000,2000); 
  RF_servo_cmd = map(RF_servo_angle,0,180,1000,2000);
  LR_servo_cmd = map(LR_servo_angle,0,180,1000,2000);
  RR_servo_cmd = map(RR_servo_angle,0,180,1000,2000);
  
  
  //Fine tune servo calibration:
  //should not be greater than like 50 or 100
  //The larger the number, the smaller the range of motion of the servos
  LF_servo_cmd += 0;
  RF_servo_cmd += 0;
  LR_servo_cmd += 0;
  RR_servo_cmd += 0;  
    
  //prevent interference    //ASSUMES LEFT-RIGHT SYMMETRICAL LIMITS
  
  if (suspPos > SUSP_INTERFERENCE_LIMIT){    //mining mode    
    frontServoLowerLimit_cmd = 1500-MINING_MAX_SERVO_ANGLE_FRONT*1000.0/180.0;
    frontServoUpperLimit_cmd = 1500+MINING_MAX_SERVO_ANGLE_FRONT*1000.0/180.0;
    rearServoLowerLimit_cmd = 1500-MINING_MAX_SERVO_ANGLE_REAR*1000.0/180.0;
    rearServoUpperLimit_cmd = 1500+MINING_MAX_SERVO_ANGLE_REAR*1000.0/180.0;
  }
  else{  //travelling mode
    frontServoLowerLimit_cmd = 1500-TRAVEL_MAX_SERVO_ANGLE_FRONT*1000.0/180.0;
    frontServoUpperLimit_cmd = 1500+TRAVEL_MAX_SERVO_ANGLE_FRONT*1000.0/180.0;
    rearServoLowerLimit_cmd = 1500-TRAVEL_MAX_SERVO_ANGLE_REAR*1000.0/180.0;
    rearServoUpperLimit_cmd = 1500+TRAVEL_MAX_SERVO_ANGLE_REAR*1000.0/180.0;
  }
    
  LF_servo_cmd = constrain(LF_servo_cmd, frontServoLowerLimit_cmd, frontServoUpperLimit_cmd);
  RF_servo_cmd = constrain(RF_servo_cmd, frontServoLowerLimit_cmd, frontServoUpperLimit_cmd);
  LR_servo_cmd = constrain(LR_servo_cmd, rearServoLowerLimit_cmd, rearServoUpperLimit_cmd);
  RR_servo_cmd = constrain(RR_servo_cmd, rearServoLowerLimit_cmd, rearServoUpperLimit_cmd);

  //prevent accidental continuous rotation: (should be already accounted for above, but it cant hurt to be safe)
  LF_servo_cmd = constrain(LF_servo_cmd, 1000, 2000);
  RF_servo_cmd = constrain(RF_servo_cmd, 1000, 2000);
  LR_servo_cmd = constrain(LR_servo_cmd, 1000, 2000);
  RR_servo_cmd = constrain(RR_servo_cmd, 1000, 2000);


  //send signals to motors
  LF_servo.writeMicroseconds(LF_servo_cmd);
  RF_servo.writeMicroseconds(RF_servo_cmd);
  LR_servo.writeMicroseconds(LR_servo_cmd);
  RR_servo.writeMicroseconds(RR_servo_cmd);

}

void setWheelSpeed() {
//this calibration was done on May 21 by Nick and JS in google drive: MAxonMappingFunction
//trendline done in externalspreadsheet

  float A = 11.798;
  float B = -3.6778;
  /*
  if (suspPos > SUSP_INTERFERENCE_LIMIT)  //go slower in mining mode
  {
    LF_motor_cmd = LF_motor_cmd/4;
    RF_motor_cmd = RF_motor_cmd/4;
    RR_motor_cmd = RR_motor_cmd/4;
    LR_motor_cmd = LR_motor_cmd/4;
  }
  */
  
  LF_motor_cmd = A*LF_wheel_rpm + B;
  RF_motor_cmd = A*RF_wheel_rpm + B;
  LR_motor_cmd = A*LR_wheel_rpm + B;
  RR_motor_cmd = A*RR_wheel_rpm + B;

  LF_motor_cmd = constrain(LF_motor_cmd, 0, 255);
  RF_motor_cmd = constrain(RF_motor_cmd, 0, 255);
  LR_motor_cmd = constrain(LR_motor_cmd, 0, 255);
  RR_motor_cmd = constrain(RR_motor_cmd, 0, 255);


  analogWrite(LF_motor_pin, LF_motor_cmd);
  analogWrite(RF_motor_pin, RF_motor_cmd);
  analogWrite(LR_motor_pin, LR_motor_cmd);
  analogWrite(RR_motor_pin, RR_motor_cmd);
}

void applyMotorEnable()
{
 digitalWrite(LF_motor_enable_pin, LF_motor_enable);
 digitalWrite(RF_motor_enable_pin, RF_motor_enable);
 digitalWrite(LR_motor_enable_pin, LR_motor_enable);
 digitalWrite(RR_motor_enable_pin, RR_motor_enable);  
}
