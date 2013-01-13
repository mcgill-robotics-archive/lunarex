//v

import SimpleOpenNI.*;
SimpleOpenNI kinect;

int closestValue; 
int closestX;
int closestY;

void setup()
{
  size(640, 480);
  kinect = new SimpleOpenNI(this);
  kinect.enableDepth();
}
// Click on the image to give it focus,
// and then press any key.

int value = 0;
void keyPressed() {
  if (value == 0) {
    line(20, 20, 80, 80);
// Saves a TIFF file named "diagonal.tif"
for(int i = 0; i < 1000000; i++) {
  
save(i + ".jpg");
  } 
  }else {
    value = 0;
  }
}
void draw()
{
  fill(value);
  rect(25, 25, 50, 50);

  closestValue = 8000; 

  kinect.update();

  // get the depth array from the kinect
  int[] depthValues = kinect.depthMap();

  // for each row in the depth image
  for(int y = 0; y < 480; y++){ 

    // look at each pixel in the row
    for(int x = 0; x < 640; x++){ 
      // pull out the corresponding value from the depth array
      int i = x + y * 640; 
      int currentDepthValue = depthValues[i];

      // if that pixel is the closest one we've seen so far
      if(currentDepthValue > 0 && currentDepthValue < closestValue){ 
        // save its value
        closestValue = currentDepthValue;
        // and save its position (both X and Y coordinates)
        closestX = x;
        closestY = y;
      }
    }
  }

  //draw the depth image on the screen
  image(kinect.depthImage(),0,0);
  
}


