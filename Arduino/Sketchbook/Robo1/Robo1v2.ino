#include <Servo.h>
#include <ros.h>
#include <std_msgs/Float32.h>
#include <arduino_msgs/ArduinoFeedback.h>

//these are init values. Can set tthem through ang_speed and lin_speed ros topics
float angSpeed = 0;
float linSpeed = 0;

ros:: NodeHandle nh;

void setAngSpeed(const std_msgs:: Float32 &ang_speed)
{angSpeed = ang_speed.data;}
void setLinSpeed(const std_msgs:: Float32 &lin_speed)
{linSpeed = lin_speed.data;}

ros:: Subscriber<std_msgs::Float32> angSub("ang_speed", &setAngSpeed);
ros:: Subscriber<std_msgs::Float32> linSub("lin_speed", &setLinSpeed);


arduino_msgs::ArduinoFeedback fb;
ros:: Publisher feedback_publisher("arduino_feedback", &fb);


Servo LF_servo, RF_servo, LR_servo, RR_servo;

int LF_motor_dir_pin = 26;
int RF_motor_dir_pin = 27;
int LR_motor_dir_pin = 28;
int RR_motor_dir_pin = 29;

int LF_motor_enable_pin = 22;
int RF_motor_enable_pin = 22;
int LR_motor_enable_pin = 22;
int RR_motor_enable_pin = 22;

int LF_motor_pin = 9;
int RF_motor_pin = 10;
int LR_motor_pin = 11;
int RR_motor_pin = 12;

boolean LF_motor_enable = 1;
boolean RF_motor_enable = 1;
boolean LR_motor_enable = 1;
boolean RR_motor_enable = 1;

//temp initialization
boolean LF_motor_dir = 1;
boolean RF_motor_dir = 1;
boolean LR_motor_dir = 1;
boolean RR_motor_dir = 1;

float LF_wheel_rpm = 0.0;
float RF_wheel_rpm = 0.0;
float LR_wheel_rpm = 0.0;
float RR_wheel_rpm = 0.0;

float TOL = 0.5;

float LF_servo_angle = 0.0;
float RF_servo_angle = 0.0;
float LR_servo_angle = 0.0;
float RR_servo_angle = 0.0;

float LF_old_servo_angle = 0.0;
float RF_old_servo_angle = 0.0;
float LR_old_servo_angle = 0.0;
float RR_old_servo_angle = 0.0;

int LF_servo_cmd = 0;
int RF_servo_cmd = 0;
int LR_servo_cmd = 0;
int RR_servo_cmd = 0;

int LF_motor_cmd = 0;
int RF_motor_cmd = 0;
int LR_motor_cmd = 0;
int RR_motor_cmd = 0;

//all values in meters
float motor_rpm;
float WHEEL_RADIUS = 0.1397;
float MIN_SPEED = 0;
//MAX_SPEED is in Revolutions per minutes
float MAX_SPEED = 20000;
float LENGTH = 0.71;
float WIDTH = 0.7219;
float DIST_TO_AXIS_A = 0.5074;
//in degrees
int MAX_ANGLE = 181;
int SEC_PER_MIN = 60;
int GEAR_RATIO = 74;

void setup()
{
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
  
  //enable motors, assumes high = enabled
  digitalWrite(LF_motor_enable_pin, LF_motor_enable);
  digitalWrite(RF_motor_enable_pin, RF_motor_enable);
  digitalWrite(LR_motor_enable_pin, LR_motor_enable);
  digitalWrite(RR_motor_enable_pin, RR_motor_enable);
  
  nh.initNode();
  nh.subscribe(angSub);
  nh.subscribe(linSub);
  nh.advertise(feedback_publisher);
}

void loop()
{ 
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
  setWheelSpeed(LF_wheel_rpm, RF_wheel_rpm, LR_wheel_rpm, RR_wheel_rpm);
  
  LF_old_servo_angle = LF_servo_angle;  
  RF_old_servo_angle = RF_servo_angle;  
  LR_old_servo_angle = LR_servo_angle;  
  RR_old_servo_angle = RR_servo_angle;
  
  
  populateFeedbackMessage();

  feedback_publisher.publish(&fb);

  nh.spinOnce();
}

void stopAll()
{
   LF_wheel_rpm = 0.0;
   RF_wheel_rpm = 0.0;
   LR_wheel_rpm = 0.0;
   RR_wheel_rpm = 0.0;
   
   digitalWrite(LF_motor_enable_pin, LF_motor_enable);
   digitalWrite(RF_motor_enable_pin, RF_motor_enable);
   digitalWrite(LR_motor_enable_pin, LF_motor_enable);
   digitalWrite(RR_motor_enable_pin, RR_motor_enable);
}

void turnOnSpot()
{
  digitalWrite(LF_motor_enable_pin, LF_motor_enable);
  digitalWrite(RF_motor_enable_pin, RF_motor_enable);
  digitalWrite(LR_motor_enable_pin, LF_motor_enable);
  digitalWrite(RR_motor_enable_pin, RR_motor_enable);
  
   LF_servo_angle = 135;
   RF_servo_angle = 45;
   LR_servo_angle = 45;
   RR_servo_angle = 135;
   
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
   
   motor_rpm = (DIST_TO_AXIS_A / WHEEL_RADIUS)*angSpeed*SEC_PER_MIN/(2*PI);
   
   LF_wheel_rpm = motor_rpm;
   RF_wheel_rpm = motor_rpm;
   LR_wheel_rpm = motor_rpm;
   RR_wheel_rpm = motor_rpm; 
}

void goStraight()
{
    digitalWrite(LF_motor_enable_pin, LF_motor_enable);
  digitalWrite(RF_motor_enable_pin, RF_motor_enable);
  digitalWrite(LR_motor_enable_pin, LR_motor_enable);
  digitalWrite(RR_motor_enable_pin, RR_motor_enable);
  
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
    
    motor_rpm = SEC_PER_MIN*linSpeed/(2*PI*WHEEL_RADIUS);
    
    LF_wheel_rpm = motor_rpm;
    RF_wheel_rpm = motor_rpm;
    LR_wheel_rpm = motor_rpm;
    RR_wheel_rpm = motor_rpm;  
}

void doAckerman()
{
  ackRadius = (abs(linSpeed)/2.0)*sin(abs(angSpeed)/2.0);
  innerFront = atan(LENGTH/(ackRadius - (WIDTH/2.0)))*180/PI;
  outerFront = atan(LENGTH/(ackRadius + (WIDTH/2.0)))*180/PI;
  innerBack = 0;
  outerBack = 0;
  

  
   if(abs(innerFront)>20)    //innerfront wheel will always have to turn more, do double if this condition is met
   {
      c = LENGTH /2.0;
      innerFront = atan(c/(ackRadius - (WIDTH/2.0)))*180/PI;
      outerFront = atan(c/(ackRadius + (WIDTH/2.0)))*180/PI; 
      innerBack = atan(c/(ackRadius -(WIDTH/2.0)))*180/PI;
      outerBack = atan(c/(ackRadius + (WIDTH/2.0)))*180/PI;
    }
    
    dir = (angSpeed * linSpeed) /abs((angSpeed * linSpeed));
    if(dir>0)  //counter clockwise
    {
      
      LF_servo_angle = 90 +innerFront;
      RF_servo_angle = 90 - outerFront;
      LR_servo_angle = 90 - innerBack;
      RR_servo_angle = 90 + outerBack;
      
      rad1 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
      rad2 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
      rad3 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
      rad4 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
    }
    else if(dir<0)  //clockwise
    {
      LF_servo_angle = 90 + outerFront;
      RF_servo_angle = 90 - innerFront;
      LR_servo_angle = 90 + innerBack;
      RR_servo_angle = 90 - outerBack;
      
      rad1 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
      rad2 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
      rad3 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
      rad4 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
    }
    Serial.println(LF_servo_angle);
    Serial.println(RF_servo_angle);
    Serial.println(LR_servo_angle);
    Serial.println(RR_servo_angle);
    
    //now for drive motor velocities
    LF_motor_speed = (rad1 / WHEEL_RADIUS) * angSpeed*SEC_PER_MIN/(2*PI);
    RF_motor_speed = (rad2 / WHEEL_RADIUS) * angSpeed*SEC_PER_MIN/(2*PI);
    LR_motor_speed = (rad3 / WHEEL_RADIUS) * angSpeed*SEC_PER_MIN/(2*PI);
    RR_motor_speed = (rad4 / WHEEL_RADIUS) * angSpeed*SEC_PER_MIN/(2*PI);
}

/*void doAckerman()
{ //Now that we know that the linear AND angular velocities are non-zero.
    //Implement ackerman or double ackerman "in motion steering algorithm" depending on how sharp a turn it is. 
      //Default single ackerman unless a front wheel angle would be above a threshold, MAX_ANGLE
      //If single ackerman generates too high an angle, recalculate with double ackerman
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
    
    float ackRadius = (abs(linSpeed)/2.0)*sin(abs(angSpeed)/2.0);
    float innerFront = atan(LENGTH/(ackRadius - (WIDTH/2.0)));
    float outerFront = atan(LENGTH/(ackRadius + (WIDTH/2.0)));
    float innerBack = 0;
    float outerBack = 0;
    
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
    LF_wheel_rpm = (rad1 / WHEEL_RADIUS) * angSpeed*SEC_PER_MIN/(2*PI);
    RF_wheel_rpm = (rad2 / WHEEL_RADIUS) * angSpeed*SEC_PER_MIN/(2*PI);
    LR_wheel_rpm = (rad3 / WHEEL_RADIUS) * angSpeed*SEC_PER_MIN/(2*PI);
    RR_wheel_rpm = (rad4 / WHEEL_RADIUS) * angSpeed*SEC_PER_MIN/(2*PI);
  }*/
  
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

void setWheelAngle(int LF_servo_angle, int RF_servo_angle, int LR_servo_angle, int RR_servo_angle)
{
  //motor numbers --> upper left = 1, upper right = 2, lower left = 3, lower right = 4
  
  
  LF_servo_cmd = map(LF_servo_angle,0,180,1000,2000); //still need to validate this mapping and might need to invert it for the front or back servos (which are mounted backwards)
  RF_servo_cmd = map(RF_servo_angle,0,180,1000,2000);
  LR_servo_cmd = map(LR_servo_angle,0,180,1000,2000);
  RR_servo_cmd = map(RR_servo_angle,0,180,1000,2000);
  
  //prevent accidental continuous rotation:
  LF_servo_cmd = constrain(LF_servo_cmd, 1000, 2000);
  RF_servo_cmd = constrain(RF_servo_cmd, 1000, 2000);
  LR_servo_cmd = constrain(LR_servo_cmd, 1000, 2000);
  RR_servo_cmd = constrain(RR_servo_cmd, 1000, 2000);
  if(abs(LF_servo_angle - LF_old_servo_angle)>TOL || abs(RR_servo_angle-RR_old_servo_angle)>TOL)
  {
    LF_servo.writeMicroseconds(LF_servo_cmd);
    RF_servo.writeMicroseconds(RF_servo_cmd);
    LR_servo.writeMicroseconds(LR_servo_cmd);
    RR_servo.writeMicroseconds(RR_servo_cmd);
  }
}

void setWheelSpeed(int LF_wheel_rpm, int RF_wheel_rpm, int LR_wheel_rpm, int RR_wheel_rpm)
{
  LF_motor_cmd = 11.7718918*LF_wheel_rpm - 3.81049;
  RF_motor_cmd = 11.7718918*RF_wheel_rpm - 3.81049;
  LR_motor_cmd = 11.7718918*LR_wheel_rpm - 3.81049;
  RR_motor_cmd = 11.7718918*RR_wheel_rpm - 3.81049;

  analogWrite(LF_motor_pin, LF_wheel_rpm);
  analogWrite(RF_motor_pin, RF_wheel_rpm);
  analogWrite(LR_motor_pin, LR_wheel_rpm);
  analogWrite(RR_motor_pin, RR_wheel_rpm);
}

void populateFeedbackMessage(){
  fb.linSpeed.data = linSpeed;
  fb.angSpeed.data = angSpeed;
  
  fb.LF_motor_enable.data = LF_motor_enable;
  fb.LF_motor_dir.data = LF_motor_dir;
  fb.LF_wheel_rpm.data = LF_wheel_rpm;
  fb.LF_motor_cmd.data = LF_motor_cmd;

  fb.LF_servo_angle.data = LF_servo_angle;
  fb.LF_servo_cmd.data = LF_servo_cmd;
  
  fb.RF_motor_enable.data = RF_motor_enable;
  fb.RF_motor_dir.data = RF_motor_dir;
  fb.RF_wheel_rpm.data = RF_wheel_rpm;
  fb.RF_motor_cmd.data = RF_motor_cmd;

  fb.RF_servo_angle.data = RF_servo_angle;
  fb.RF_servo_cmd.data = RF_servo_cmd;
  
  fb.LR_motor_enable.data = LR_motor_enable;
  fb.LR_motor_dir.data = LR_motor_dir;
  fb.LR_wheel_rpm.data = LR_wheel_rpm;
  fb.LR_motor_cmd.data = LR_motor_cmd;

  fb.LR_servo_angle.data = LR_servo_angle;
  fb.LR_servo_cmd.data = LR_servo_cmd;
  
  fb.RR_motor_enable.data = RR_motor_enable;
  fb.RR_motor_dir.data = RR_motor_dir;
  fb.RR_wheel_rpm.data = RR_wheel_rpm;
  fb.RR_motor_cmd.data = RR_motor_cmd;

  fb.RR_servo_angle.data = RR_servo_angle;
  fb.RR_servo_cmd.data = RR_servo_cmd;
}
