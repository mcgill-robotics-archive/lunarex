#include <Servo.h>
#include <ros.h>
#include <std_msgs/Float32.h>

//these are init values. Can set tthem through ang_speed and lin_speed ros topics
float angSpeed = 0;
float linSpeed = 100000;

//100000; is 80% of 5v, with 14.4V.. about 7.48rpm

//0 - 20 000 rpm on motor

ros:: NodeHandle nh;

void setAngSpeed(const std_msgs:: Float32 &ang_speed)
{angSpeed = ang_speed.data;}
void setLinSpeed(const std_msgs:: Float32 &lin_speed)
{linSpeed = lin_speed.data;}

ros:: Subscriber<std_msgs::Float32> angSub("ang_speed", &setAngSpeed);
ros:: Subscriber<std_msgs::Float32> linSub("lin_speed", &setLinSpeed);

Servo LF_servo, RF_servo, LR_servo, RR_servo;

int LF_motor_dir_pin = 26;
int RF_motor_dir_pin = 27;
int LR_motor_dir_pin = 28;
int RR_motor_dir_pin = 29;

int LF_motor_enable_pin = 22;
int RF_motor_enable_pin = 22;
int LR_motor_enable_pin = 22;
int RR_motor_enable_pin = 22;

//motor numbers --> upper left = 1, upper right = 2, lower left = 3, lower right = 4
int LF_motor_speed_pin = 9;
int RF_motor_speed_pin = 10;
int LR_motor_speed_pin = 11;
int RR_motor_speed_pin = 12;

//temp initialization
boolean LF_motor_dir = 1;
boolean RF_motor_dir = 1;
boolean LR_motor_dir = 1;
boolean RR_motor_dir = 1;

float LF_motor_speed = 0.0;
float RF_motor_speed = 0.0;
float LR_motor_speed = 0.0;
float RR_motor_speed = 0.0;

float LF_servo_angle = 0.0;
float RF_servo_angle = 0.0;
float LR_servo_angle = 0.0;
float RR_servo_angle = 0.0;

float wheelSpeed;
float WHEEL_RADIUS = 0.15;
float MIN_SPEED = 0;
float MAX_SPEED = 1;
float LENGTH = 0;
float WIDTH = 0;
float DIST_TO_AXIS_A = 0;
int MAX_ANGLE = 181;

void setup()
{
  pinMode(LF_motor_speed_pin, OUTPUT);
  pinMode(RF_motor_speed_pin, OUTPUT);
  pinMode(LR_motor_speed_pin, OUTPUT);
  pinMode(RR_motor_speed_pin, OUTPUT);

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
  
  //enable motors, assumes high = enabled
  digitalWrite(LF_motor_enable_pin, HIGH);
  digitalWrite(RF_motor_enable_pin, HIGH);
  digitalWrite(LR_motor_enable_pin, HIGH);
  digitalWrite(RR_motor_enable_pin, HIGH);
  
  nh.initNode();
  nh.subscribe(angSub);
  nh.subscribe(linSub);
}

void loop()
{
     nh.spinOnce();
  
  if (linSpeed == 0 && angSpeed == 0)
  {stopAll();}
  else if(linSpeed == 0)
  {turnOnSpot();}
  else if(angSpeed == 0)
  {goStraight();}
  else if(angSpeed!= 0 && linSpeed!=0)
  {doAckerman();}
  
  setWheelDirection(LF_motor_dir, RF_motor_dir, LR_motor_dir, RR_motor_dir);
  setWheelAngle(LF_servo_angle, RF_servo_angle, LR_servo_angle, RR_servo_angle);
  setWheelSpeed(LF_motor_speed, RF_motor_speed, LR_motor_speed, RR_motor_speed);
  
}

void stopAll()
{
   LF_motor_speed = 0.0;
   RF_motor_speed = 0.0;
   LR_motor_speed = 0.0;
   RR_motor_speed = 0.0;
   
     digitalWrite(LF_motor_enable_pin, LOW);
  digitalWrite(RF_motor_enable_pin, LOW);
  digitalWrite(LR_motor_enable_pin, LOW);
  digitalWrite(RR_motor_enable_pin, LOW);
}

void turnOnSpot()
{
    digitalWrite(LF_motor_enable_pin, HIGH);
  digitalWrite(RF_motor_enable_pin, HIGH);
  digitalWrite(LR_motor_enable_pin, HIGH);
  digitalWrite(RR_motor_enable_pin, HIGH);
  
   LF_servo_angle = 135;
   RF_servo_angle = 45;
   LR_servo_angle = 135;
   RR_servo_angle = 45;
   
   if(angSpeed>0)
   {   
      //to be replaced with code compatible with controller and hardware conditions
      //we assume here that 1 = forward, 0 = backward //but what about the 1 and 0? -Nick Speal
     LF_motor_dir = 0;
     RF_motor_dir = 1;
     LR_motor_dir = 0;
     RR_motor_dir = 1;
   }
   else if(angSpeed < 0);
   {
     LF_motor_dir = 1;
     RF_motor_dir = 0;
     LR_motor_dir = 1;
     RR_motor_dir = 0;
   }    
   
   wheelSpeed = linSpeed/(2*PI*WHEEL_RADIUS);
   wheelSpeed = map(wheelSpeed, MIN_SPEED, MAX_SPEED, 0, 255);
   
   LF_motor_speed = wheelSpeed;
   RF_motor_speed = wheelSpeed;
   LR_motor_speed = wheelSpeed;
   RR_motor_speed = wheelSpeed; 
}

void goStraight()
{
    digitalWrite(LF_motor_enable_pin, HIGH);
  digitalWrite(RF_motor_enable_pin, HIGH);
  digitalWrite(LR_motor_enable_pin, HIGH);
  digitalWrite(RR_motor_enable_pin, HIGH);
  
  //set all wheel directions to straight, then impliment drive
    
    //setWheelAngle() call moved to end from here
    LF_servo_angle = 90;
    RF_servo_angle = 90;
    LR_servo_angle = 90;
    RR_servo_angle = 90;
    
    if(linSpeed>0) //changed from >= to > because '==' has a different case
    {
      //setWheelDirection() call moved to end from here
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
    
    wheelSpeed = linSpeed/(2*PI*WHEEL_RADIUS);
    wheelSpeed = map(wheelSpeed, MIN_SPEED, MAX_SPEED, 0, 255);
    
    LF_motor_speed = wheelSpeed;
    RF_motor_speed = wheelSpeed;
    LR_motor_speed = wheelSpeed;
    RR_motor_speed = wheelSpeed;  
}

void doAckerman()
{ //Now that we know that the linear AND angular velocities are non-zero.
    //Implement ackerman or double ackerman "in motion steering algorithm" depending on how sharp a turn it is. 
      //Default single ackerman unless a front wheel angle would be above a threshold, MAX_ANGLE
      //If single ackerman generates too high an angle, recalculate with double ackerman
     digitalWrite(LF_motor_enable_pin, HIGH);
  digitalWrite(RF_motor_enable_pin, HIGH);
  digitalWrite(LR_motor_enable_pin, HIGH);
  digitalWrite(RR_motor_enable_pin, HIGH);
   
   
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
    
    float ackRadius = (abs(linSpeed)/2.0)*sin(abs(angSpeed)/2.0);
    float innerFront = atan(LENGTH/(ackRadius - (WIDTH/2.0)));
    float outerFront = atan(LENGTH/(ackRadius + (WIDTH/2.0)));
    float innerBack = 0;
    float outerBack = 0;
    
    innerFront = innerFront*180/PI;
    outerFront = outerFront*180/PI;
    int R1 = sqrt(pow(ackRadius,2) - pow(DIST_TO_AXIS_A, 2));
    int rad1 = sqrt(pow(LENGTH, 2) + pow(R1-WIDTH/2, 2));
    int rad2 = sqrt(pow(LENGTH, 2) + pow(R1+WIDTH/2, 2));
    int rad3 = R1 - WIDTH/2;
    int rad4 = R1 + WIDTH/2;
    
     if(innerFront>MAX_ANGLE)    //innerfront wheel will always have to turn more, do double if this condition is met
    {
       float c = LENGTH /2.0;
       innerFront = atan(c/(ackRadius - (WIDTH/2.0)));
       outerFront = atan(c/(ackRadius + (WIDTH/2.0))); 
       innerBack = atan(c/(ackRadius - (WIDTH/2.0)));
       outerBack = atan(c/(ackRadius + (WIDTH/2.0)));
       
       innerFront = innerFront*180/PI;
       outerFront = outerFront*180/PI;
       innerBack= innerBack*180/PI;
       outerBack = outerBack*180/PI;
    }
    
    float dir = (angSpeed * linSpeed) /abs((angSpeed * linSpeed));  //Will return +/- 1 for CCW or CW, respectively (note this variable is distinct from LF_motor_dir, RF_motor_dir, etc)
    
    if(dir>0)  //counter clockwise
    {
      
      LF_servo_angle = 90 - innerFront;
      RF_servo_angle = 90 - outerFront;
      LR_servo_angle = 90 + innerBack;
      RR_servo_angle = 90 + outerBack;
      
      rad1 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
      rad2 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
      rad3 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
      rad4 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
    }
    else if(dir<0)  //clockwise
    {
      LF_servo_angle = 90 + outerFront;
      RF_servo_angle = 90 + innerFront;
      LR_servo_angle = 90 - outerBack;
      RR_servo_angle = 90 - outerBack;
      
      rad1 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
      rad2 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
      rad3 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
      rad4 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
    }
    
    //now for drive motor velocities
    LF_motor_speed = (rad1 / WHEEL_RADIUS) * angSpeed;
    RF_motor_speed = (rad2 / WHEEL_RADIUS) * angSpeed;
    LR_motor_speed = (rad3 / WHEEL_RADIUS) * angSpeed;
    RR_motor_speed = (rad4 / WHEEL_RADIUS) * angSpeed;
  }
  
void setWheelDirection(int LF_motor_dir, int RF_motor_dir, int LR_motor_dir, int RR_motor_dir)
{
  //forward or backwards for drive wheels
  digitalWrite(LF_motor_dir_pin, LF_motor_dir);
  digitalWrite(RF_motor_dir_pin, RF_motor_dir);
  digitalWrite(LR_motor_dir_pin, LR_motor_dir);
  digitalWrite(RR_motor_dir_pin, RR_motor_dir);
}

void setWheelAngle(int LF_servo_angle, int RF_servo_angle, int LR_servo_angle, int RR_servo_angle)
{
  //motor numbers --> upper left = 1, upper right = 2, lower left = 3, lower right = 4
  
  int LF_servo_cmd = map(LF_servo_angle,0,180,1000,2000); //still need to validate this mapping and might need to invert it for the front or back servos (which are mounted backwards)
  int RF_servo_cmd = map(RF_servo_angle,0,180,1000,2000);
  int LR_servo_cmd = map(LR_servo_angle,0,180,1000,2000);
  int RR_servo_cmd = map(RR_servo_angle,0,180,1000,2000);
  
  LF_servo.writeMicroseconds(LF_servo_cmd);
  RF_servo.writeMicroseconds(RF_servo_cmd);
  LR_servo.writeMicroseconds(LR_servo_cmd);
  RR_servo.writeMicroseconds(RR_servo_cmd);
}

void setWheelSpeed(int LF_motor_speed, int RF_motor_speed, int LR_motor_speed, int RR_motor_speed)
{
  analogWrite(LF_motor_speed_pin, LF_motor_speed);
  analogWrite(RF_motor_speed_pin, RF_motor_speed);
  analogWrite(LR_motor_speed_pin, LR_motor_speed);
  analogWrite(RR_motor_speed_pin, RR_motor_speed);
}
