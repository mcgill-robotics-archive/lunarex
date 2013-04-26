float angSpeed = 1;
float linSpeed = 1;

float LF_servo_angle = 0.0;
float RF_servo_angle = 0.0;
float LR_servo_angle = 0.0;
float RR_servo_angle = 0.0;

float WHEEL_RADIUS = 0.1397;
float MIN_SPEED = 0;
//MAX_SPEED is in Revolutions per minutes
float MAX_SPEED = 20000;
float LENGTH = 0.71;
float WIDTH = 0.7219;
float DIST_TO_AXIS_A = 0.5074;
//in degrees
int MAX_ANGLE = 35;
int SEC_PER_MIN = 60;
int GEAR_RATIO = 74;

void setup()
{Serial.begin(9600);}

void loop()
{

  float ackRadius = abs(linSpeed)/abs(angSpeed);
  Serial.print("Ackradius: ");
  Serial.println(ackRadius);
  float innerFront = atan(LENGTH/(ackRadius - (WIDTH/2.0)))*180/PI;
  float outerFront = atan(LENGTH/(ackRadius + (WIDTH/2.0)))*180/PI;
  Serial.print("Innerfront1 :");
  Serial.println(innerFront);
  float innerBack = 0;
  float outerBack = 0;

  float R1 = sqrt(pow(ackRadius,2) - pow(DIST_TO_AXIS_A, 2));
  float rad1 = sqrt(pow(LENGTH, 2) + pow(R1-WIDTH/2, 2));
  float rad2 = sqrt(pow(LENGTH, 2) + pow(R1+WIDTH/2, 2));
  float rad3 = R1 - WIDTH/2;
  float rad4 = R1 + WIDTH/2;
   
  if(innerFront>MAX_ANGLE)    //innerfront wheel will always have to turn more, do double if this condition is met
  {
     float c = LENGTH /2.0;
     innerFront = atan(c/(ackRadius - (WIDTH/2.0)))*180/PI;
     outerFront = atan(c/(ackRadius + (WIDTH/2.0)))*180/PI; 
     innerBack = atan(c/(ackRadius - (WIDTH/2.0)))*180/PI;
     outerBack = atan(c/(ackRadius + (WIDTH/2.0)))*180/PI;
       
  }

  float dir = (angSpeed * linSpeed) /abs((angSpeed * linSpeed));  //Will return +/- 1 for CCW or CW, respectively (note this variable is distinct from LF_motor_dir, RF_motor_dir, etc)
    
   if(dir>0.0)  //counter clockwise
   {
    
      LF_servo_angle = 90 - innerFront;
      Serial.println(LF_servo_angle);
      RF_servo_angle = 90 - outerFront;
      LR_servo_angle = 90 + innerBack;
      RR_servo_angle = 90 + outerBack;
     
      rad1 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
      rad2 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
      rad3 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
      rad4 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
    }
    else if(dir<0.0)  //clockwise
    {
      LF_servo_angle = 90.0 + outerFront;
      RF_servo_angle = 90.0 + innerFront;
      LR_servo_angle = 90.0 - outerBack;
      RR_servo_angle = 90.0 - outerBack;
      
      
      
      rad1 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
      rad2 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
      rad3 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius+WIDTH/2, 2));
      rad4 = sqrt(pow(LENGTH/2, 2) + pow(ackRadius-WIDTH/2, 2));
    }
    
}
