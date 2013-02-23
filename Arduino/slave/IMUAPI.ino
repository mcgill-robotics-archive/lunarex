/*=====================================================================
//  Name: IMUAPI
//
//  Authors:
//    Jean-Sébastien Déry
//
//  Purpose:
//    It is giving a higher-level API to use the IMU
//===================================================================*/


// right now those two functions are useless, but I need to arange the code a little.
void setHeading(float newHeading) {
  yaw = newHeading;
}

float getHeading() {
  return (yaw);
}

void resetIMU() {
  Serial.begin(115200);
  
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
  
  // Activates the refresh, and sends confirmation to laptop.
  activeIMU = true;
  str_msg = OK_IMU_RESET;
  chatter.publish(&str_msg);
}

void updateIMU() {
  if((millis()-imuTimer)>=20)  // Main loop runs at 50Hz
  {
    counter++;
    imuTimerOld = imuTimer;
    imuTimer=millis();
    if (imuTimer>imuTimer) {
      G_Dt = (imuTimer-imuTimerOld)/1000.0;    // Real time of loop run. We use this on the DCM algorithm (gyro integration time)
    } else {
      G_Dt = 0;
    }

    Read_Gyro();   // This read gyro data
    Read_Accel();     // Read I2C accelerometer
    
    if (counter > 5) { // Read compass data at 10Hz... (5 loop runs)
      counter=0;
      Read_Compass();    // Read I2C magnetometer
      Compass_Heading(); // Calculate magnetic heading  
    }

    // Gathering data.
    Matrix_update();
    Normalize();
    Drift_correction();
    Euler_angles();
   
    //printdata();
    
    // Publish the IMU heading.
    sendHeading.data = yaw;
    pub_temp.publish(&sendHeading);
  }
}


