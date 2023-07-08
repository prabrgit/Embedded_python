
void setup() {
  pinMode(8,OUTPUT);
  Serial.begin(9600);
}
void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.print("You sent me: ");
    Serial.println(data);
    if(data == "1"){
     digitalWrite(8, HIGH); 
     
    }
    if(data == "2"){
     digitalWrite(8, LOW);
     
    }
  }
}