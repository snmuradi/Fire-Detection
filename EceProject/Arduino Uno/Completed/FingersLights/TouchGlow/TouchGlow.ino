int ledPin1 = 13;  
int ledPin2 = 12;  
int ledPin3 = 11;  
int ledPin4 = 10;  
int ledPin5 = 9;

void setup() {
  Serial.begin(9600);  
  pinMode(ledPin1, OUTPUT);  
  pinMode(ledPin2, OUTPUT);  
  pinMode(ledPin3, OUTPUT);  
  pinMode(ledPin4, OUTPUT);  
  pinMode(ledPin5, OUTPUT);  
}

void loop() {
  if (Serial.available()) {
    int incomingByte = Serial.read();
    if (incomingByte == '0') {
      digitalWrite(ledPin1, LOW);  // Turn LED off
      digitalWrite(ledPin2, LOW);  // Turn LED off
      digitalWrite(ledPin3, LOW);  // Turn LED off
      digitalWrite(ledPin4, LOW);  // Turn LED off
      digitalWrite(ledPin5, LOW);  // Turn LED off
    } else if (incomingByte == '1') {
      digitalWrite(ledPin1, HIGH);  // Turn LED off
      digitalWrite(ledPin2, LOW);  // Turn LED off
      digitalWrite(ledPin3, LOW);  // Turn LED off
      digitalWrite(ledPin4, LOW);  // Turn LED off
      digitalWrite(ledPin5, LOW);  // Turn LED off
    } else if (incomingByte == '2') {
      digitalWrite(ledPin1, HIGH);  // Turn LED off
      digitalWrite(ledPin2, HIGH);  // Turn LED off
      digitalWrite(ledPin3, LOW);  // Turn LED off
      digitalWrite(ledPin4, LOW);  // Turn LED off
      digitalWrite(ledPin5, LOW);  // Turn LED off
    } else if (incomingByte == '3') {
      digitalWrite(ledPin1, HIGH);  // Turn LED off
      digitalWrite(ledPin2, HIGH);  // Turn LED off
      digitalWrite(ledPin3, HIGH);  // Turn LED off
      digitalWrite(ledPin4, LOW);  // Turn LED off
      digitalWrite(ledPin5, LOW);  // Turn LED off
    } else if (incomingByte == '4') {
      digitalWrite(ledPin1, HIGH);  // Turn LED off
      digitalWrite(ledPin2, HIGH);  // Turn LED off
      digitalWrite(ledPin3, HIGH);  // Turn LED off
      digitalWrite(ledPin4, HIGH);  // Turn LED off
      digitalWrite(ledPin5, LOW);  // Turn LED off
    } else if (incomingByte == '5') {
      digitalWrite(ledPin1, HIGH);  // Turn LED off
      digitalWrite(ledPin2, HIGH);  // Turn LED off
      digitalWrite(ledPin3, HIGH);  // Turn LED off
      digitalWrite(ledPin4, HIGH);  // Turn LED off
      digitalWrite(ledPin5, HIGH);  // Turn LED off
    }
  }
}
