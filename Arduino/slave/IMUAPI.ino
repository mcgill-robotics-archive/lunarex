/*=====================================================================
//  Name: IMUAPI
//
//  Authors:
//    Jean-Sébastien Déry
//
//  Purpose:
//    It is giving a higher-level API to use the IMU
//===================================================================*/

void setHeading(float newHeading) {
  yaw = newHeading;
}

float getHeading() {
  return (yaw);
}

void resetIMU() {
  I2C_Init();

  delay(1500);
 
  Accel_Init();
  Compass_Init();
  Gyro_Init();
  
  delay(20);
  
  // Taking some reading for calibration.
  for(int i=0;i<32;i++) {
    Read_Gyro();
    Read_Accel();
    for(int y=0; y<6; y++) {
      AN_OFFSET[y] += AN[y];
    }
    delay(20);
  }
  
  // Adjusting the offset.
  for(int y=0; y<6; y++) {
    AN_OFFSET[y] = AN_OFFSET[y]/32;
  }
    
  AN_OFFSET[5]-=GRAVITY*SENSOR_SIGN[5];
  
  //Serial.println("Offset:");
  for(int y=0; y<6; y++) {
    Serial.print(AN_OFFSET[y]);
    Serial.print(";");
  }
  
  delay(2000);
  
  imuTimer=millis();
  delay(20);
  counter=0;
}

void updateIMU() {
  
}


