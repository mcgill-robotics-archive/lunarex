// Simply write something to each motor

#include <Servo.h> 
 
//these are just sent to defaults so we dont get in the way of the servos
Servo suspActuatorRight;
Servo suspActuatorLeft;
Servo dumpActuator;
Servo doorActuatorLeft;
Servo doorActuatorRight;

//actual servos
Servo lr;
Servo lf;
Servo rf;
Servo rr;

void setup() {
  // servo pins valid Wed May 8 night
  
  rf.attach(3);
  rr.attach(5);
  lr.attach(4);
  lf.attach(2);
}

void loop() {
  
  analogWrite(6, 255);  //suspension actuators extended ('up') =0    retracted ('down') = 255
  analogWrite(7, 0);  //dumpActuator retracted 'down' = 255,    up would be 0
  analogWrite(8, 0);    //auger stopped
  analogWrite(13, 255);  //door actuators retracted, 'closed' = 0      'open' = 255
  
  int val = 1500 ;   //1000 is left, 1500 straight, 2000 right
  rf.writeMicroseconds(val);
  rr.writeMicroseconds(val);
  lr.writeMicroseconds(val);
  lf.writeMicroseconds(val);
  
  delay(200);
}

