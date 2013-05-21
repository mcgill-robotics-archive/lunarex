#include <Servo.h> 


Servo wheel;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  //myservo.attach(9);

//these are just sent to defaults so we dont get in the way of the servos  
  analogWrite(6, 0);  //suspension actuators extended ('up')
  analogWrite(7, 0);  //dumpActuator retracted 'down'
  //analogWrite(8, 10);    //auger stopped
  analogWrite(13, 255);  //door actuators retracted, 'closed'


  // servo pins valid Wed May 8 night
  digitalWrite(33, HIGH);  //enable lf
  
}

void loop() {
  // if there's any serial available, read it:
  while (Serial.available() > 0) {
    int val = Serial.parseInt();
    Serial.println(val);
    
    analogWrite(12, val); //lf
  }
  delay(200);
}


