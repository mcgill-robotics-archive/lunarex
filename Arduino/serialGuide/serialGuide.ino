/*
 
 This program receives ASCII characters 1,2,3, or 4 via serial.
 It then controls servo speeds accordingly.
 If '5' is sent, it toggles the position of the scoop.
 
 */
#include <Servo.h>

int inByte = 0;         // incoming serial byte
int leftSpeed = 0;
int rightSpeed = 0;
boolean scoopOpen = false;

Servo leftWheel;
Servo rightWheel;
Servo scoopServo;

void setup()
{
  // start serial port at 9600 bps:
  Serial.begin(115200);
  leftWheel.attach(11);
  rightWheel.attach(3);
  scoopServo.attach(6); //is this the right pin?
  go(leftSpeed, rightSpeed); 
}

void loop()
{
  // if we get a valid byte, read analog ins:
  if (Serial.available() > 0) {
    // get incoming byte:
    inByte = Serial.read();
    switch (inByte) {
      case '1':
        //forward
        leftSpeed++;
        rightSpeed++;
        break;
      case '2':
        //backward
        leftSpeed--;
        rightSpeed--;
        break;
      case '3':
        //left
        leftSpeed--;
        rightSpeed++;
        break;
      case '4':
        //right
        leftSpeed++;
        rightSpeed--;
        break;
      case '5':
        //toggle scoop
        scoopOpen = !scoopOpen;
        toggleScoop(scoopOpen);
        break;
      default:
        //none of the above
        Serial.print('invalid character');
        break;  
      
    } //end switch
  go(leftSpeed, rightSpeed);  
  }//end if serial available
  
}//end void loop

void go(int leftSpeed, int rightSpeed) {
  int maxRange = 10;  //max speed in either direction
  
  //reject bad outputs
  if(leftSpeed>maxRange) leftSpeed=maxRange;
  if(rightSpeed>maxRange) rightSpeed=maxRange;
  if(leftSpeed<-maxRange) leftSpeed= -minRange;
  if(rightSpeed<-maxRange) rightSpeed= -minRange;
  
  
  //transform to servo values
  leftOutput = 90-leftSpeed; //left wheel is installed backwards
  rightOutput = 90 + rightSpeed;

  
  //write to servos
  leftWheel.write(leftOutput);  
  rightWheel.write(rightOutput);
}

void toggleScoop(boolean scoopOpen){
  if (scoopOpen)
  {
     scoopServo.write(0);  //calibrate numbers needed, should be closed position here
  }
  else
  {
    scoopServo.write(60);  //calibrate numbers needed, should be opened position here
  }
}

