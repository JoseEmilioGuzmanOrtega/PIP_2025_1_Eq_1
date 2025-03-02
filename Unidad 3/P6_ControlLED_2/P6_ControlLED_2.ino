int led=13; //LED
void setup() {
  // put your setup code here, to run once:
pinMode(led,OUTPUT); // OUTPUT cuando Actuadores Digitales o INPUT
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(led,1);  //1 = Alto/HIGH o 0 = Bajo/LOW
delay(500);
digitalWrite(led,0);
delay(500);
}
