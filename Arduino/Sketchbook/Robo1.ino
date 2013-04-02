
#include <Servo.h>
#include <ros.h>
#include <std_msgs/Float32.h>


Servo upLeftServo, upRightServo, boLeftServo, boRightServo;

int directionPin1 = 3;
int directionPin2 = 4;
int directionPin3 = 5;
int directionPin4 = 6;

int enablePin1 = 7;
int enablePin2 = 8;
int enablePin3 = 9;
int enablePin4 = 10;

//motor numbers --> upper left = 1, upper right = 2, lower left = 3, lower right = 4
int motorPin1 = 11;
int motorPin2 = 12;
int motorPin3 = 13;
int motorPin4 = 14;

boolean dir1 = 1;
boolean dir2 = 1;
boolean dir3 = 1;
boolean dir4 = 1;

float linSpeed = 0;
float angSpeed = 0;

float motorSpeed1 = 0.0;
float motorSpeed2 = 0.0;
float motorSpeed3 = 0.0;
float motorSpeed4 = 0.0;

float motorAng1 = 0.0;
float motorAng2 = 0.0;
float motorAng3 = 0.0;
float motorAng4 = 0.0;

float wheelSpeed;
float wheelRad = 1;
float minSpeed = 0;
float maxSpeed = 1;

float length = 0;
float width = 0;
float distToAxisA = 0;
int maxAngle = 0;

void setup()
{
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);
  
  pinMode(enablePin1, OUTPUT);
  pinMode(enablePin2, OUTPUT);
  pinMode(enablePin3, OUTPUT);
  pinMode(enablePin4, OUTPUT);
  
  //enable motors, assumes high = enabled
  digitalWrite(enablePin1, HIGH);
  digitalWrite(enablePin2, HIGH);
  digitalWrite(enablePin3, HIGH);
  digitalWrite(enablePin4, HIGH);
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
  
  setWheelDirection(dir1, dir2, dir3, dir4);
  setWheelAngle(motorAng1, motorAng2, motorAng3, motorAng4);
  setWheelSpeed(motorSpeed1, motorSpeed2, motorSpeed3, motorSpeed4);
  
}

void stopAll()
{
   motorSpeed1 = 0.0;
   motorSpeed2 = 0.0;
   motorSpeed3 = 0.0;
   motorSpeed4 = 0.0;
}

void turnOnSpot()
{
   motorAng1 = 135;
   motorAng2 = 45;
   motorAng3 = 135;
   motorAng4 = 45;
   
   if(angSpeed>0)
   {   
      //to be replaced with code compatible with controller and hardware conditions
      //we assume here that 1 = forward, 0 = backward //but what about the 1 and 0? -Nick Speal
     dir1 = 0;
     dir2 = 1;
     dir3 = 0;
     dir4 = 1;
   }
   else if(angSpeed < 0);
   {
     dir1 = 1;
     dir2 = 0;
     dir3 = 1;
     dir4 = 0;
   }    
   
   wheelSpeed = linSpeed/(2*PI*wheelRad);
   wheelSpeed = map(wheelSpeed, minSpeed, maxSpeed, 0, 255);
   
   motorSpeed1 = wheelSpeed;
   motorSpeed2 = wheelSpeed;
   motorSpeed3 = wheelSpeed;
   motorSpeed4 = wheelSpeed; 
}

void goStraight()
{
  //set all wheel directions to straight, then impliment drive
    
    //setWheelAngle() call moved to end from here
    motorAng1 = 90;
    motorAng2 = 90;
    motorAng3 = 90;
    motorAng4 = 90;
    
    if(linSpeed>0) //changed from >= to > because '==' has a different case
    {
      //setWheelDirection() call moved to end from here
      dir1 = 1;
      dir2 = 1;
      dir3 = 1;
      dir4 = 1;
    }
    else if(linSpeed < 0)
    {
      dir1 = 0;
      dir2 = 0;
      dir3 = 0;
      dir4 = 0;
    }
    
    wheelSpeed = linSpeed/(2*PI*wheelRad);
    wheelSpeed = map(wheelSpeed, minSpeed, maxSpeed, 0, 255);
    
    motorSpeed1 = wheelSpeed;
    motorSpeed2 = wheelSpeed;
    motorSpeed3 = wheelSpeed;
    motorSpeed4 = wheelSpeed;  
}

void doAckerman()
{ //Now that we know that the linear AND angular velocities are non-zero.
    //Implement ackerman or double ackerman "in motion steering algorithm" depending on how sharp a turn it is. 
      //Default single ackerman unless a front wheel angle would be above a threshold, maxAngle
      //If single ackerman generates too high an angle, recalculate with double ackerman
   if(linSpeed < 0) //changed from <= to < because '==' has a different case
    {
      dir1 = 0;
      dir2 = 0;
      dir3 = 0;
      dir4 = 0;
    }
    
    else if(linSpeed > 0)
    {
      dir1 = 1;
      dir2 = 1;
      dir3 = 1;
      dir4 = 1;
    }
    
    float ackRadius = (abs(linSpeed)/2.0)*sin(abs(angSpeed)/2.0);
    float innerFront = atan(length/(ackRadius - (width/2.0)));
    float outerFront = atan(length/(ackRadius + (width/2.0)));
    float innerBack = 0;
    float outerBack = 0;
    
    innerFront = innerFront*180/PI;
    outerFront = outerFront*180/PI;
    int R1 = sqrt(pow(ackRadius,2) - pow(distToAxisA, 2));
    int rad1 = sqrt(pow(length, 2) + pow(R1-width/2, 2));
    int rad2 = sqrt(pow(length, 2) + pow(R1+width/2, 2));
    int rad3 = R1 - width/2;
    int rad4 = R1 + width/2;
    
     if(innerFront>maxAngle)    //innerfront wheel will always have to turn more, do double if this condition is met
    {
       float c = length /2.0;
       innerFront = atan(c/(ackRadius - (width/2.0)));
       outerFront = atan(c/(ackRadius + (width/2.0))); 
       innerBack = atan(c/(ackRadius - (width/2.0)));
       outerBack = atan(c/(ackRadius + (width/2.0)));
       
       innerFront = innerFront*180/PI;
       outerFront = outerFront*180/PI;
       innerBack= innerBack*180/PI;
       outerBack = outerBack*180/PI;
    }
    
    float dir = (angSpeed * linSpeed) /abs((angSpeed * linSpeed));  //Will return +/- 1 for CCW or CW, respectively (note this variable is distinct from dir1, dir2, etc)
    
    if(dir>0)  //counter clockwise
    {
      
      motorAng1 = 90 - innerFront;
      motorAng2 = 90 - outerFront;
      motorAng3 = 90 + innerBack;
      motorAng4 = 90 + outerBack;
      
      rad1 = sqrt(pow(length/2, 2) + pow(ackRadius-width/2, 2));
      rad2 = sqrt(pow(length/2, 2) + pow(ackRadius+width/2, 2));
      rad3 = sqrt(pow(length/2, 2) + pow(ackRadius-width/2, 2));
      rad4 = sqrt(pow(length/2, 2) + pow(ackRadius+width/2, 2));
    }
    else if(dir<0)  //clockwise
    {
      motorAng1 = 90 + outerFront;
      motorAng2 = 90 + innerFront;
      motorAng3 = 90 - outerBack;
      motorAng4 = 90 - outerBack;
      
      rad1 = sqrt(pow(length/2, 2) + pow(ackRadius+width/2, 2));
      rad2 = sqrt(pow(length/2, 2) + pow(ackRadius-width/2, 2));
      rad3 = sqrt(pow(length/2, 2) + pow(ackRadius+width/2, 2));
      rad4 = sqrt(pow(length/2, 2) + pow(ackRadius-width/2, 2));
    }
    
    //now for drive motor velocities
    motorSpeed1 = (rad1 / wheelRad) * angSpeed;
    motorSpeed2 = (rad2 / wheelRad) * angSpeed;
    motorSpeed3 = (rad3 / wheelRad) * angSpeed;
    motorSpeed4 = (rad4 / wheelRad) * angSpeed;
  }
  
void setWheelDirection(int dir1, int dir2, int dir3, int dir4)
{
  //forward or backwards for drive wheels
  digitalWrite(directionPin1, dir1);
  digitalWrite(directionPin2, dir2);
  digitalWrite(directionPin3, dir3);
  digitalWrite(directionPin4, dir4);
}

void setWheelAngle(int motorAng1, int motorAng2, int motorAng3, int motorAng4)
{
  //motor numbers --> upper left = 1, upper right = 2, lower left = 3, lower right = 4
  
  int servoCmd1 = map(motorAng1,0,180,1000,2000); //still need to validate this mapping and might need to invert it for the front or back servos (which are mounted backwards)
  int servoCmd2 = map(motorAng2,0,180,1000,2000);
  int servoCmd3 = map(motorAng3,0,180,1000,2000);
  int servoCmd4 = map(motorAng4,0,180,1000,2000);
  
  upLeftServo.writeMicroseconds(servoCmd1);
  upRightServo.writeMicroseconds(servoCmd2);
  boLeftServo.writeMicroseconds(servoCmd3);
  boRightServo.writeMicroseconds(servoCmd4);
}

void setWheelSpeed(int motorSpeed1, int motorSpeed2, int motorSpeed3, int motorSpeed4)
{
  analogWrite(motorPin1, motorSpeed1);
  analogWrite(motorPin2, motorSpeed2);
  analogWrite(motorPin3, motorSpeed3);
  analogWrite(motorPin4, motorSpeed4);
}
