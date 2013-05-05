#include <ros.h>
#include <std_msgs/Float32.h>
#include <Servo.h>
//#include <PID_v1.h>
#include <math.h>

//Last updated March 28-29 by Nick
//here are a couple comments on what I did as well as suggestions for changes to be made:

//Added a couple comments for clarity
//mapped the angle from 0-180 degrees to 1000-2000 ms (is this measured clockwise from the -x axis, seen from above?)
//moved the pin declarations so they are all together
//in Navigate() added "STOP" condition for 0 angular AND linear velocity
//for drive motor directions, discrepency between comments and code in terms of 0vs1 or 1vs2, variable names are dir1, dir2 etc
//In the Navigate function for the cases of 0 ang vel or 0 lin vel, removed the call to setWheelAngle() and made it so this is only c
//lled once at the end of the function
// in "turn on spot" case, changed if angSpeed <= 0 to if <0 because angSpeed shouldnt be zero if turning on the spot. Made a similar
//change several times througout for clarity.
//motorSpeed, dir, motorAng should be initialized
//do we want a specific frequency of calls to Navigate() ?
//changed include Math.h to math.h


//global variables
float wheelRad;
float width;
float length;
float distToAxisA;
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
int motorPin1 = 9;
int motorPin2 = 10;
int motorPin3 = 11;
int motorPin4 = 12;

float minSpeed; //presumably 0... -Nick Speal
float maxSpeed; //will require calibration. I think this is the measured speed that corresponds to full voltage
float maxAngle; //Threshold to step up from single ackerman to double ackerman

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
{
  angSpeed = ang_speed.data;
}
void setLinSpeed(const std_msgs:: Float32 &lin_speed)
{
  linSpeed = lin_speed.data;
}

//subscribers for the angular and linear speed
ros:: Subscriber<std_msgs::Float32> angSpeedSub("Set_Angular_Speed", &setAngSpeed);
ros:: Subscriber<std_msgs::Float32> linSpeedSub("Set_Linear_Speed", &setLinSpeed);


float motorSpeed1, motorSpeed2, motorSpeed3, motorSpeed4;
float motorAng1, motorAng2, motorAng3, motorAng4;
short dir1, dir2, dir3, dir4;
int steering, dir, c;
int state[3];
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
  // delay(some number here (in milliseconds)  Do we want a certain rate for this code? Or should it jjust call navigate() as frequentl
  //as possible?
}



void navigate(float angSpeed, float linSpeed)
{
  //motor numbers --> upper left = 1, upper right = 2, lower left = 3, lower right = 4

  //if no linear speed, turn about axis in center of robot, may impliment bandwidth for minimum linear speed 
  if (linSpeed == 0 && angSpeed == 0) //stop case
  {
    //Drive motors should stop and the servos should maintain their position

    //no change to motorAng
    //no change to dir1,dir2, etc
    motorSpeed1 = 0;
    motorSpeed2 = 0;
    motorSpeed3 = 0;
    motorSpeed4 = 0;

  }

  else if(linSpeed == 0) //turn on spot case
  {
    //rotate all motors to 45 degrees
    //upper left and bottom right are 45 degrees clockwise - needs to be changed based on servo PWM
    //placeholders, to be changed
    //bottom left and upper right need to be set to 45 degrees CCW

    //I think these angles are defined as clockwise from the -x axis, as seen from the top? -Nick Speal

    motorAng1 = 135;
    motorAng2 = 45;
    motorAng3 = 135;
    motorAng4 = 45;
    //set CCW to positive, CW to negative
    if(angSpeed>0)
    {   
      //to be replaced with code compatible with controller and hardware conditions
      //we assume here that 1 = forward, 2 = backward //but what about the 1 and 0? -Nick Speal
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


    //now set motor speed based on wheel radius, wheel distance from axis, values for max speed
    distToAxisA = distToCenter;
    wheelSpeed = angSpeed*distToAxisA/wheelRad;
    wheelSpeed = map(wheelSpeed, minSpeed, maxSpeed, 0, 255);

    motorSpeed1 = wheelSpeed;
    motorSpeed2 = wheelSpeed;
    motorSpeed3 = wheelSpeed;
    motorSpeed4 = wheelSpeed;
  }

  //if angular speed is 0, go straight, may impliment bandwidth for minimum angular speed
  else if(angSpeed == 0)
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


  else 
  {
    //Now that we know that the linear AND angular velocities are non-zero.
    //Implement ackerman or double ackerman "in motion steering algorithm" depending on how sharp a turn it is. 
    //Default single ackerman unless a front wheel angle would be above a threshold, maxAngle
    //If single ackerman generates too high an angle, recalculate with double ackerman


    //first determine direction of drive motors
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

    //single ackerman
    ackRadius = (abs(linSpeed)/2.0)*sin(abs(angSpeed)/2.0);
    innerFront = atan(length/(ackRadius - (width/2.0)));
    outerFront = atan(length/(ackRadius + (width/2.0)));
    innerBack = 0;
    outerBack = 0;

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

    //Check which direction the robot is rotating. Then the steering angles will be opposite, depending on the linear velocity.
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

  //All angles, speeds, directions are chosen for the given case. Now send the signals:
  setWheelDirection(dir1, dir2, dir3, dir4);
  setWheelAngle(motorAng1, motorAng2, motorAng3, motorAng4);
  setWheelSpeed(motorSpeed1, motorSpeed2, motorSpeed3, motorSpeed4);
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

