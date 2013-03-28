#include <ros.h>
#include <std_msgs/Float32.h>
#include <Servo.h>
#include <PID_v1.h>
#include <Math.h>

//global variables
float wheelRad;
float width;
float length;
float distToAxisA, distToAxisB, distToAxisC, distToAxisD;
Servo upLeftServo, upRightServo, boLeftServo boRightServo;
int directionPin1 = 3;
int directionPin2 = 4;
int directionPin3 = 5;
int directionPin4 = 6;

int enablePin1 = 7;
int enablePin2 = 8;
int enablePin3 = 9;
int enablePin4 = 10;

float minSpeed;
float maxSpeed;

float ackRadius;
float leftAckAngle, rightAckAngle;
float innerFront, innerBack, outerFront, outerBack;

//make a node on the arduino
ros:: NodeHandle nh;

//variables to store angular and linear speed/velocity
float angSpeed = 0;
float linSpeed = 0;

//methods to change the angular speed and velocity from a std_msg of type float32
void setAngSpeed(const std_msgs:: Float32 &ang_speed)
{angSpeed = ang_speed.data;}
void setLinSpeed(const std_msgs:: Float32 &lin_speed)
{linSpeed = lin_speed.data;}

//subscribers for the angular and linear speed
ros:: Subscriber<std_msgs::Float32> angSpeedSub("Set_Angular_Speed", &setAngSpeed);
ros:: Subscriber<std_msgs::Float32> linSpeedSub("Set_Linear_Speed", &setLinSpeed);

//Setup for the PID for each motor

int motorPin1 = 9;
int motorPin2 = 10;
int motorPin3 = 11;
int motorPin4 = 12;

//setup, initialize node, serial and PID stuff
void setup()
{
  //ROS node initialization
  nh.initNode();
  nh.subscribe(angSpeedSub);
  nh.subscribe(linSpeedSub);
  
  //inputs and outputs
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

//the meat of the program, does all management of stuff
void loop()
{
  nh.spinOnce();
  navigate(angSpeed, linSpeed);
}

void navigate(float angSpeed, float linSpeed)
{
  //motor numbers --> upper left = 1, upper right = 2, lower left = 3, lower right = 4
  
  //if no linear speed, turn about axis in center of robot, may impliment bandwidth for minimum linear speed 
  if(linSpeed == 0)
  {
    //rotate all motors to 45 degrees
    //upper left and bottom right are 45 degrees clockwise - needs to be changed based on servo PWM
    //placeholders, to be changed
    setWheelDirection(135, 45, 135, 45);
    upLeftServo.write(135);
    boRightServo.write(135);
    
    //bottom left and upper right need to be set to 45 degrees CCW
    //place holder values, to be changed
    upRightServo.write(45);
    boLeftServo.write(45);
    
    //set CCW to positive, CW to negative
    if(angSpeed>0)
    {   
      //to be replaced with code compatible with controller and hardware conditions
      //we assume here that HIGH = forward, LOW = backward
      digitalWrite(directionPin1, LOW);
      digitalWrite(directionPin2, HIGH);
      digitalWrite(directionPin3, LOW);
      digitalWrite(directionPin4, HIGH);
    }
    else if(angSpeed <= 0);
    {
      digitalWrite(directionPin1, HIGH);
      digitalWrite(directionPin2, LOW);
      digitalWrite(directionPin3, HIGH);
      digitalWrite(directionPin4, LOW);
    }
    
    //now set motor speed based on wheel radius, wheel distance from axis, values for max speed
    distToAxisA = distToCenter;
    wheelSpeed = angSpeed*distToAxisA/wheelRad;
    wheelSpeed = map(wheelSpeed, minSpeed, maxSpeed, 0, 255);
    Setpoint1, Setpoint2, Setpoint3, Setpoint4 = wheelSpeed;
    
  }
  
  //if angular speed is 0, go straight, may impliment bandwidth for minimum angular speed
  else if(angSpeed == 0)
  {
    //set all wheel directions to straight, then impliment drive
    upLeftServo.write(90);
    upRightServo.write(90);
    boLeftServo.write(90);
    boRightServo.write(90);
    
    if(linSpeed>=0)
    {
      digitalWrite(directionPin1, HIGH);
      digitalWrite(directionPin2, HIGH);
      digitalWrite(directionPin3, HIGH);
      digitalWrite(directionPin4, HIGH);
    }
    else if(linSpeed < 0)
    {
      digitalWrite(directionPin1, LOW);
      digitalWrite(directionPin2, LOW);
      digitalWrite(directionPin3, LOW);
      digitalWrite(directionPin4, LOW);
    }
    
    wheelSpeed = linSpeed/(2*PI*wheelRad);
    wheelSpeed = map(wheelSpeed, minSpeed, maxSpeed, 0, 255);
    Setpoint1, Setpoint2, Setpoint3, Setpoint4 = wheelSpeed;
  }
  
  //otherwise, do turning in motion algorithm, ackerman or double ackerman
  else
  {
    //assume that the wheels will not turn more than 35 degrees
    //determine radius of "ackerman circle", see what degree the wheels would need to turn
    //if greater than 35, do double ackerman
    
    //first determine direction
    float dir = (angSpeed * linSpeed) /abs((angSpeed * linSpeed);
    //single ackerman
    ackRadius = (abs(linSpeed)/2.0)*sin(abs(angSpeed)/2.0);
    innerFront = atan(length/(ackRadius - (width/2.0)));
    outerFront = atan(length/(ackRadius + (width/2.0)));
    innerBack = 0;
    outerBack = 0;
    innerFront = innerFront*180/PI;
    outerFront = outerFront*180/PI;
    
    if(innerFront>35)    //innerfront wheel will always have to turn more, do double if this condition is met
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
    
    if((dir > 0 && angVel >0) || (dir<0 && angVel<0))
    {
      upLeftServo.write(90 - innerFront);
      upRightServo.write(90 - outerFront);
      boLeftServo.write(90 + innerBack);
      boRightServo.write(90 + innerBack);
    }
    else
    {
      upLeftServo.write(90 + outerFront);
      upRightServo.write(90 + outerFront);
      boLeftServo.write(90 - innerBack);
      boRightServo.write(90 - innerBack);
    }
    
    //now for velocity
    
  }
 
  analogWrite(Output1, motorPin1);
  analogWrite(Output2, motorPin2);
  analogWrite(Output3, motorPin3);
  analogWrite(Output4, motorPin4);
}

float 
