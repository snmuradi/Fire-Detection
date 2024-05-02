#include<Servo.h>

Servo x, y;
int width = 640, height = 480;  // total resolution of the video
int xPos = 90, yPos = 90;  // initial positions of both Servos
bool isLastLeft=false;
int bazaar=2;

void setup() {
  Serial.begin(9600);
  x.attach(9);
  y.attach(10);
  pinMode(bazaar,OUTPUT);
  // Serial.print(width);
  //Serial.print("\t");
  //Serial.println(height);
  x.write(xPos);
  y.write(yPos);
}
const int angle = 1;   // degree of increment or decrement

void loop() {
  if (Serial.available() > 0)
  {
    int x_mid, y_mid;
    if (Serial.read() == 'X')
    {
      x_mid = Serial.parseInt();  // read center x-coordinate
      if (Serial.read() == 'Y')
        y_mid = Serial.parseInt(); // read center y-coordinate
    }

    digitalWrite(bazaar, HIGH);

    /* adjust the servo within the squared region if the coordinates
        is outside it
    */
    if (x_mid > width / 2 + 30)
      xPos += angle;
    if (x_mid < width / 2 - 30)
      xPos -= angle;
    if (y_mid < height / 2 + 30)
      yPos -= angle;
    if (y_mid > height / 2 - 30)
      yPos += angle;


    // if the servo degree is outside its range
    if (xPos >= 180)
      xPos = 180;
    else if (xPos <= 0)
      xPos = 0;
    if (yPos >= 180)
      yPos = 180;
    else if (yPos <= 0)
      yPos = 0;

    x.write(xPos);
    y.write(yPos);

    // used for testing
    //Serial.print("\t");
    // Serial.print(x_mid);
    // Serial.print("\t");
    // Serial.println(y_mid);
  }else{
    digitalWrite(bazaar, LOW);
    if(xPos<=1){
      isLastLeft=true;
    }
    if(xPos>=179){
      isLastLeft=false;
    }
    if(!isLastLeft){
      xPos--;
    }
    if(isLastLeft){
      xPos++;
    }
    x.write(xPos);
    delay(50);
  }
}
