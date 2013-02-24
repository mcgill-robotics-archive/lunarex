#include <ros.h>                //import ros
#include <std_msgs/Int8.h>      //import int8 to receive int data type from ros
#include <std_msgs/String.h>    //import to use strings
#include <PID_v1.h>		//Pulvic inflammation disease

int motoPin;
int inputPin;
int encoderPin = 3;
int maxSpeed = 400;

ros:: Nodehandle nh;
ros:: Subscriber<std_msgs::Int8> sub("set_speed", &messageCb);
std_msgs:: String str_msg;
std_msgs:: Int8 int_msg;

ros:: Publisher chatter("chatter", &str_msg);

char received[14] = "Received data.";
char hello[10] = "Connected.";
char finished[17] = "Completed action.";

double setpoint, input, output;
double kp = 1;
double ki = 1;
double kd = 1;

PID myPID(&input, &output, &setpoint, kp, ki, kd, DIRECT);



void setup()
{
  nh.initNode();
  nh.advertise(chatter);
  nh.subscribe(sub);
  str_msg = hello;
  chatter.publish(&str_msg);
  myPid.SetMode(AUTOMATIC);
  attachInterrupt(1, increment, CHANGE);    //1 means pin 3, only pins 2 and 3 support interrupts
}

void messageCb(const std_msgs:: Int8 &cmd_msg)
{
  setPoint = cmd_msg.data;
  str_msg.data = received;
  chatter.publish(&str_msg);
  nh.spinOnce();
  input = getSpeed();
  myPID.Compute();
  analogWrite(output, motoPin);
}

void loop()
{
  nh.spinOnce();
  input = getSpeed();
  int_msg.data = input;
  chatter.publish(&int_msg);
  myPID.Compute();
  analogWrite(motoPin, output);
}

double getSpeed() 
{
int time1 = 0;
int time2 = 0;
double angVel = 0;

counter = 0;


 while(1)
  {
    
    if(counter == 0)
    {
      
      time1=millis();
    }
    if(counter >= 5)
    {
      
      time2 = millis();
      angVel = counter*(2*PI/90)*(1000)/(time2-time1);
      
      return map(angVel, 0, maxSpeed, 0, 255);
    }
   
  }
  
}

void increment()
{
  ++counter;
  
}


