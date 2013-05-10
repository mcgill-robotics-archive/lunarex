#include <Servo.h>
#include <ros.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Bool.h>
#include <std_msgs/UInt8.h>

float angSpeed = 2;
float linSpeed = 1;
float dumpPos = 255; //down as default
float suspPos = 0; //up as default
float doorPos = 0;
float augerSpeed = 0;

Servo LF_servo, RF_servo, LR_servo, RR_servo;
Servo augerSudoServo;

//these 4 pins are arbitrary as of april 27
int suspActuator_pin = 6;
int dumpActuator_pin = 7;
int augerMotor_pin = 8;
int doorPos_pin = 13;

int LF_motor_dir_pin = 27;
int RF_motor_dir_pin = 29;
int LR_motor_dir_pin = 31;
int RR_motor_dir_pin = 33;

int LF_motor_enable_pin = 26;
int RF_motor_enable_pin = 28;
int LR_motor_enable_pin = 30;
int RR_motor_enable_pin = 32;

int LF_motor_pin = 9;
int RF_motor_pin = 10;
int LR_motor_pin = 11;
int RR_motor_pin = 12;

boolean LF_motor_enable = 1;
boolean RF_motor_enable = 1;
boolean LR_motor_enable = 1;
boolean RR_motor_enable = 1;

boolean LF_motor_dir = 1;
boolean RF_motor_dir = 1;
boolean LR_motor_dir = 1;
boolean RR_motor_dir = 1;

float LF_wheel_rpm = 0.0;
float RF_wheel_rpm = 0.0;
float LR_wheel_rpm = 0.0;
float RR_wheel_rpm = 0.0;

float LF_servo_angle = 90.0;
float RF_servo_angle = 90.0;
float LR_servo_angle = 90.0;
float RR_servo_angle = 90.0;

float LF_old_servo_angle = 90.0;
float RF_old_servo_angle = 90.0;
float LR_old_servo_angle = 90.0;
float RR_old_servo_angle = 90.0;

int LF_servo_cmd = 0;
int RF_servo_cmd = 0;
int LR_servo_cmd = 0;
int RR_servo_cmd = 0;

int LF_motor_cmd = 0;
int RF_motor_cmd = 0;
int LR_motor_cmd = 0;
int RR_motor_cmd = 0;

float motor_rpm;

//-----------------constants
float WHEEL_RADIUS = 0.1397;
float MIN_SPEED = 0;
float MAX_SPEED = 20000; // in Revolutions per minutes
float LENGTH = 0.71;
float WIDTH = 0.7219;
float DIST_TO_AXIS_A = 0.5074;
int MAX_ANGLE = 35; //in degrees; ratio of lin/ang = 1.5

int SEC_PER_MIN = 60;
int GEAR_RATIO = 74;

float TOL = 0.5;
float ANG_STOP_THRESH = 2.0;
float LIN_STOP_THRESH = 0.9;

int SUSP_INTERFERENCE_LIMIT = 150; //command sent to suspension actuators. values greater than this correspond to mining
float MINING_MAX_SERVO_ANGLE_FRONT = 0;
float MINING_MAX_SERVO_ANGLE_REAR = 30;

float TRAVEL_MAX_SERVO_ANGLE_FRONT = 50;
float TRAVEL_MAX_SERVO_ANGLE_REAR = 50;

void setup()
{
  Serial.begin(9600);
  
  // ===== Driving and Steering ====
  pinMode(LF_motor_pin, OUTPUT);
  pinMode(RF_motor_pin, OUTPUT);
  pinMode(LR_motor_pin, OUTPUT);
  pinMode(RR_motor_pin, OUTPUT);

  LF_servo.attach(2);
  RF_servo.attach(3);
  LR_servo.attach(4);
  RR_servo.attach(5);
  
  pinMode(LF_motor_enable_pin, OUTPUT);
  pinMode(RF_motor_enable_pin, OUTPUT);
  pinMode(LR_motor_enable_pin, OUTPUT);
  pinMode(RR_motor_enable_pin, OUTPUT);

  pinMode(LF_motor_dir_pin, OUTPUT);
  pinMode(RF_motor_dir_pin, OUTPUT);
  pinMode(LR_motor_dir_pin, OUTPUT);
  pinMode(RR_motor_dir_pin, OUTPUT);
}

void loop()
{ 
  miningAckerman();
  
}

void miningAckerman()
{ 
  digitalWrite(LF_motor_enable_pin, LF_motor_enable);
  digitalWrite(RF_motor_enable_pin, RF_motor_enable);
  digitalWrite(LR_motor_enable_pin, LR_motor_enable);
  digitalWrite(RR_motor_enable_pin, RR_motor_enable);
   
   
  if(linSpeed < 0) //changed from <= to < because '==' has a different case
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
    

  float ackRadius = abs(linSpeed)/abs(angSpeed);
  float innerFront = 0;
  float outerFront = 0;
  float innerBack = atan(LENGTH/(ackRadius - (WIDTH/2.0)))*180/PI;
  float outerBack = atan(LENGTH/(ackRadius + (WIDTH/2.0)))*180/PI;
  
  float R1 = sqrt(pow(ackRadius,2) - pow(DIST_TO_AXIS_A, 2));
  
  float rad1 = 0;
  float rad2 = 0;
  float rad3 = 0;
  float rad4 = 0;
    
    
  float dir = (angSpeed * linSpeed) /abs((angSpeed * linSpeed));  //Will return +/- 1 for CCW or CW, respectively (note this variable is distinct from LF_motor_dir, RF_motor_dir, etc)
    
  if(dir>0.0)  //counter clockwise
  {
      LF_servo_angle = 90 - innerFront;
      RF_servo_angle = 90 - outerFront;
      LR_servo_angle = 90 + innerBack;
      RR_servo_angle = 90 + outerBack;
  
      if(innerFront == 0.0)
	    {
   	 	    
   	 	    rad1 = R1 - WIDTH/2;
   	 	    rad2 = R1 + WIDTH/2;
   	 	    rad3 = sqrt(pow(LENGTH, 2) + pow(R1-WIDTH/2, 2));
  	 	    rad4 = sqrt(pow(LENGTH, 2) + pow(R1+WIDTH/2, 2));
	    }

	    else
      {
          rad1 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
          rad2 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
		      rad3 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
		      rad4 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
      }
  }
  
  else if(dir<0.0)  //clockwise
  {

      LF_servo_angle = 90.0 + outerFront;
      RF_servo_angle = 90.0 + innerFront;
      LR_servo_angle = 90.0 - outerBack;
      RR_servo_angle = 90.0 - outerBack;
      
	    if(innerFront == 0.0)
	    {
   	     	R1 = sqrt(pow(ackRadius,2) - pow(DIST_TO_AXIS_A, 2));
   	     	rad1 = R1 + WIDTH/2;
   	     	rad2 = R1 - WIDTH/2;
   	     	rad3 = sqrt(pow(LENGTH, 2) + pow(R1+WIDTH/2, 2));
  	     	rad4 = sqrt(pow(LENGTH, 2) + pow(R1-WIDTH/2, 2));
	    }

	    else
	    {
		      rad1 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
		      rad2 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
	  	    rad3 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
	  	    rad4 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
	    }
  
  }
    
    //now for drive motor velocities
    LF_wheel_rpm = (rad1 / WHEEL_RADIUS) * angSpeed*SEC_PER_MIN/(2*PI);
    RF_wheel_rpm = (rad2 / WHEEL_RADIUS) * angSpeed*SEC_PER_MIN/(2*PI);
    LR_wheel_rpm = (rad3 / WHEEL_RADIUS) * angSpeed*SEC_PER_MIN/(2*PI);
    RR_wheel_rpm = (rad4 / WHEEL_RADIUS) * angSpeed*SEC_PER_MIN/(2*PI);
    
    Serial.println(innerBack);
}
  

void setWheelDirection(boolean LF_motor_dir, boolean RF_motor_dir, boolean LR_motor_dir, boolean RR_motor_dir)
{
  RF_motor_dir = !RF_motor_dir;
  RR_motor_dir = !RR_motor_dir;
  
  //forward or backwards for drive wheels
  digitalWrite(LF_motor_dir_pin, LF_motor_dir);
  digitalWrite(RF_motor_dir_pin, RF_motor_dir);
  digitalWrite(LR_motor_dir_pin, LR_motor_dir);
  digitalWrite(RR_motor_dir_pin, RR_motor_dir);
}
void setWheelAngle(float LF_servo_angle, float RF_servo_angle, float LR_servo_angle, float RR_servo_angle)
{
  //motor numbers --> upper left = 1, upper right = 2, lower left = 3, lower right = 4
  
  
  //initialize limits on what commands can be sent
  int frontServoLowerLimit_cmd = 1000;
  int frontServoUpperLimit_cmd = 2000;
  int rearServoLowerLimit_cmd = 1000;
  int rearServoUpperLimit_cmd = 2000;
  
  LF_servo_cmd = map(LF_servo_angle,0,180,1000,2000); 
  RF_servo_cmd = map(RF_servo_angle,0,180,1000,2000);
  LR_servo_cmd = map(LR_servo_angle,0,180,1000,2000);
  RR_servo_cmd = map(RR_servo_angle,0,180,1000,2000);
    
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
    LR_servo_cmd = constrain(LR_servo_cmd, rearServoLowerLimit_cmd, frontServoUpperLimit_cmd);
    RR_servo_cmd = constrain(RR_servo_cmd, rearServoLowerLimit_cmd, frontServoUpperLimit_cmd);


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

/* 

THE FOLLOWING AVOIDS CHANGING THE PWM SIGNAL IF THE OLD SERVO ANGLE WAS THE SAME. THE PROBLEM WE WERE HAVING WAS A GROUND PLANE ISSUE - NOT THIS
IF WE UNCOMMENT THIS BLOCK, WE NEED TO REMOVE THE writeMicroseconds COMMANDS ABOVE

   if(abs(LF_servo_angle - LF_old_servo_angle)>TOL || abs(RR_servo_angle-RR_old_servo_angle)>TOL)
  if(abs(LF_servo_angle - LF_old_servo_angle)>TOL || abs(RR_servo_angle-RR_old_servo_angle)>TOL)
  {
    LF_servo.writeMicroseconds(LF_servo_cmd);
    RF_servo.writeMicroseconds(RF_servo_cmd);
    LR_servo.writeMicroseconds(LR_servo_cmd);
    RR_servo.writeMicroseconds(RR_servo_cmd);
  }
}

*/
}

void setWheelSpeed(int LF_wheel_rpm, int RF_wheel_rpm, int LR_wheel_rpm, int RR_wheel_rpm) {
  //THESE CALIBRATION CONSTANTS NEED TO BE BETTER DOCUMENTED!!
  //I think they were determined on wheels that are floating in the air to map rpm to a 0-255 command
  //I think the process of coming up with these constants is in google drive somewhere, in the second sheet of a spreadsheet
  //-Nick

  float A = 11.7718918;
  float B = -3.81049;
  
  
  LF_motor_cmd = A*LF_wheel_rpm + B;
  RF_motor_cmd = A*RF_wheel_rpm + B;
  LR_motor_cmd = A*LR_wheel_rpm + B;
  RR_motor_cmd = A*RR_wheel_rpm + B;

  analogWrite(LF_motor_pin, LF_wheel_rpm);
  analogWrite(RF_motor_pin, RF_wheel_rpm);
  analogWrite(LR_motor_pin, LR_wheel_rpm);
  analogWrite(RR_motor_pin, RR_wheel_rpm);
}
