#include <ros.h>
#include <std_msgs/Float32.h>

float angSpeed = 0;
float linSpeed = 0;

ros:: NodeHandle nh;

void setAngSpeed(const std_msgs:: Float32 &ang_speed)
{angSpeed = ang_speed.data;}
void setLinSpeed(const std_msgs:: Float32 &lin_speed)
{linSpeed = lin_speed.data;}

ros:: Subscriber<std_msgs::Float32> angSub("ang_speed", &setAngSpeed);
ros:: Subscriber<std_msgs::Float32> linSub("lin_peed", &setLinSpeed);

void setup()
{
  nh.initNode();
  nh.subscribe(angSpeedSub);
  nh.subscribe(linSpeedSub);
}

void loop()
{
   nh.spinOnce();
}


