void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);  //Habiita un modulo VART - Se mide en Baudios
}

void loop() {
  // put your main code here, to run repeatedly:
Serial.println("hola mundo");  //Transmicion de Datos
delay(100); //ms
}
