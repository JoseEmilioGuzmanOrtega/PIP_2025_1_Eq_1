int led 1 = 5;
int led 2 = 6;
int led 3 = 7;
int led 4 = 8;
void setup() {
  // put your setup code here, to run once:
pinMode(led1,OUTPUT);
pinMode(led2,OUTPUT);
pinMode(led3,OUTPUT);
pinMode(led4,OUTPUT);
Serial.begin(9600);
Serial.setTimeout(10);
}
int v;
void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()>0){
  v=Serial.readString().toInt();
  digitalWrite(led1,v);
  digitalWrite(led2,v);
  digitalWrite(led3,v);
  digitalWrite(led4,v);
}
delay(100);
}
