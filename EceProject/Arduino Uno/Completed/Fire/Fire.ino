int Ll = 13;  
int Uu = 12;  
int Rr = 11;  
int Dd = 10;

void setup() {
  Serial.begin(9600);  
  pinMode(Ll, OUTPUT);  
  pinMode(Uu, OUTPUT);  
  pinMode(Rr, OUTPUT);  
  pinMode(Dd, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    int incomingByte = Serial.read();
    
    if (incomingByte == 'L') {
      digitalWrite(Ll, HIGH);
    } else{
      digitalWrite(Ll, LOW);
    }
    if (incomingByte == 'U') {
      digitalWrite(Uu, HIGH);
    } else{
      digitalWrite(Uu, LOW);
    }
    if (incomingByte == 'R') {
      digitalWrite(Rr, HIGH);
    } else{
      digitalWrite(Rr, LOW);
    }
    if (incomingByte == 'D') {
      digitalWrite(Dd, HIGH);
    } else{
      digitalWrite(Dd, LOW);
    }



    if (incomingByte == 'Q') {
      digitalWrite(Ll, HIGH);
      digitalWrite(Uu, HIGH);
    }
    if (incomingByte == 'E') {
      digitalWrite(Uu, HIGH);
      digitalWrite(Rr, HIGH);
    }
    if (incomingByte == 'X') {
      digitalWrite(Rr, HIGH);
      digitalWrite(Dd, HIGH);
    }
    if (incomingByte == 'Z') {
      digitalWrite(Dd, HIGH);
      digitalWrite(Ll, HIGH);
    }


  }
}
