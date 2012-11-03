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
  Serial.begin(9600);
  leftWheel.attach(11);
  rightWheel.attach(3);
  scoopServo.attach(6); //is this the right pin?
  establishContact();  // send a byte to establish contact until receiver responds
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
    
  Serial.print("Left Speed: ");
  Serial.print(leftSpeed);
  Serial.print('\n');
  Serial.print("Right Speed: ");
  Serial.print(rightSpeed);  
  Serial.print("\n \n");  
  go(leftSpeed, rightSpeed);  
  }//end if serial available
  
}//end void loop

void establishContact() {
  Serial.print("Waiting for input")
  while (Serial.available() <= 0) {
    Serial.print('.');   // send a capital A
    delay(300);
  }
  Serial.print("\n Contact Established! \n\n")
}

void go(int leftSpeed, int rightSpeed) {
 leftWheel.write(90 -leftSpeed);  //left wheel is installed backwards
 rightWheel.write(rightSpeed + 90);
}

void toggleScoop(boolean scoopOpen){
  if (scoopOpen)
  {
     scoopServo.write(0)  //calibrate numbers needed, should be closed position here
  }
  else
  {
    scoopServo.write(60)  //calibrate numbers needed, should be opened position here
  }
}

