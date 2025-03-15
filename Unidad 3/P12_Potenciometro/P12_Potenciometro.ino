int pot = A0; // Pin Analogico - A0 a A5 (Sensores)
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
// No requiere PinMode
}

void loop() {
  // put your main code here, to run repeatedly:
int v = analogRead(pot); // ADC (n = bits de resolución) 2^n = [0-1023]
Serial.println(v);
delay(100);
}
