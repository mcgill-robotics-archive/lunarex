#include <ros.h>                //import ros
#include <std_msgs/Int8.h>      //import int8 to receive int data type from ros
#include <std_msgs/String.h>    //import to use strings
#include <PID_v1.h>		//Pulvic inflammation disease

int enablePin1, enablePin2, enablePin3, enablePin4;
int speed1, speed2, speed3, speed4;
int directionPin1, directionPin2, directionPin3, directionPin4;

int input1, setpoint1, ouput1;
int input2, setpoint2, ouput2;
int input3, setpoint3, ouput3;
int input4, setpoint4, ouput4;
int kp, ki, kd;

PID motor1(&input1, &output1, &setpoint1, kp, ki, kd, DIRECT);
PID motor2(&input2, &output2, &setpoint2, kp, ki, kd, DIRECT);
PID motor3(&input3, &output3, &setpoint3, kp, ki, kd, DIRECT);
PID motor4(&input4, &output4, &setpoint4, kp, ki, kd, DIRECT);

ros:: Nodehandle nh;

ros:: Subscriber<std_msgs::Int8> speedSub("set_speed", &speedControl);
ros:: Subscriber<std_msgs::String> directionSub("set_direction", &directionControl);
ros:: Subscriber<std_msgs::String> enableSub("enable",&enableControl);

ros:: Publisher chatter("chatter", &str_msg);

char received[14] = "Received data.";
char hello[10] = "Connected.";
char finished[17] = "Completed action.";

void setup()
{
  nh.initNode();
  nh.advertise(chatter);
  nh.subscribe(speedSub);
  nh.subscribe(directionSub);
  nh.subscribe(enableSub);
  
  str_msg = hello;
  chatter.publish(&str_msg);
  
  motor1.SetMode(AUTOMATIC);
  motor2.SetMode(AUTOMATIC);
  motor3.SetMode(AUTOMATIC);
  motor4.SetMode(AUTOMATIC);
}

void speedControl(const std_msgs:: Int8 &speed_msg)
{}

void directionControl(const std_msgs:: String &direction_msg)
{}

void enableControl(const std_msgs:: String &enable_msg)
{}

void loop()
{
  nh.spinOnce();
  
  getSpeed();
  motor1.Compute();
  motor2.Compute();
  motor3.Compute();
  motor4.Compute();
  
  analogWrite(speed1, output1);
  analogWrite(speed2, output2);
  analogWrite(speed3, output3);
  analogWrite(speed4, output4);
  
}

void getSpeed()
{}
