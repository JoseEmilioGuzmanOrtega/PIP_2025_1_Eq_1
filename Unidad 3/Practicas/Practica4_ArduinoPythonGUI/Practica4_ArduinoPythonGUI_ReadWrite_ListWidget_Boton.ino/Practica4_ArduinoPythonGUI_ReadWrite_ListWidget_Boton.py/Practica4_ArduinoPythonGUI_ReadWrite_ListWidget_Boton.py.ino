const int sensorPin0 = A0;
const int sensorPin1 = A1;
const int sensorPin2 = A2;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int valorSensor0 = analogRead(sensorPin0);
  int valorSensor1 = analogRead(sensorPin1);
  int valorSensor2 = analogRead(sensorPin2);

  String dataString = String(valorSensor0) + '@' + String(valorSensor1) + '@' + String(valorSensor2) + '@';

  Serial.println(dataString);

  delay(200);
}
