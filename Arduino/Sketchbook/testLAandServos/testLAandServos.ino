//Accepts a number between 800 and 2200 via serial and sends it to the servo
//I've explained the mapping of these numbers to angles at the bottom

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
float value;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  //myservo.attach(9);
  
  
  lf.attach(2);
  rf.attach(3);
  lr.attach(4);
  rr.attach(5);
  lf.writeMicroseconds(1500);
  rf.writeMicroseconds(1500);
  lr.writeMicroseconds(1500);
  rr.writeMicroseconds(1500);
  
  

  analogWrite(7, 255);  //dumpActuator retracted 'down'
  analogWrite(8, 0);    //auger stopped
  analogWrite(13, 0);  //door actuators retracted, 'closed'
  analogWrite(6, 0);
  Serial.println("waiting for value...");
  Serial.flush();
          
  // servo pins valid Wed May 8 night
  
  
}

void loop() {
  
//  if (Serial.available()) {
  //  value = Serial.parseFloat();
   // Serial.println(value);
    //lf.writeMicroseconds(value);
  //}
  
  analogWrite(6, 0);  //suspension actuators extended ('up')
  delay(4000);
  analogWrite(6, 255);
  delay(4000);
  
  lf.writeMicroseconds(1500);
  rf.writeMicroseconds(1500);
  lr.writeMicroseconds(1500);
  rr.writeMicroseconds(1500);
  
  
  
  
  /*
  // if there's any serial available, read it:
  while (Serial.available() > 0) {
    int val = Serial.parseInt();
    Serial.println(val);

    rf.writeMicroseconds(val);
    rr.writeMicroseconds(val);
    lr.writeMicroseconds(val);
    lf.writeMicroseconds(val);
    
  }
  delay(200);
  */
  
}


/*

HOW WRITEMICROSECONDS() WORKS WITH MEGASERVOS
---------------------------------------------


servo.attach() writes 93º, or approx 1500 usec
writemicroseconds() takes an argument sort of between 0 and 3000

Numbers between approx 900 and 2100 correspond to 0 and 180 physical degrees, respectively, but they write differently if you query Servo.read() you get something like 44 to 151 degrees

numbers just outside of that range correspond to continuous rotation in opposite directions.

800 will rotate continuously CCW, 2200 will rotate continuously CW

If spinning CCW after an 800 command, 900 will stop it in spot (with a small delay for communication)
if spinning CW after a 2200 command, 2100 will stop it in spot

If you mix and match the above, it will spin 180 deg. and then stop.

Numbers just outside of the 800-2100 range correspond to slow continuous rotation

*/







