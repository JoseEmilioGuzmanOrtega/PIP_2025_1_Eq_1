int led1 = 2;
int led2 = 3;
int led3 = 4;
int led4 = 5;
int led5 = 6;
int led6 = 7;
int led7 = 8;
int led8 = 9;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  pinMode(led7, OUTPUT);
  pinMode(led8, OUTPUT);
  Serial.begin(9600);
  Serial.println("Ingresa un numero decimal entre 0 y 255:");
}

void loop() {

  if (Serial.available() > 0) {
    int numero = Serial.parseInt();
    Serial.print("Numero ingresado: ");
    Serial.println(numero);

  digitalWrite(led1, (numero >> 0) & 1);
  digitalWrite(led2, (numero >> 1) & 1);
  digitalWrite(led3, (numero >> 2) & 1);
  digitalWrite(led4, (numero >> 3) & 1);
  digitalWrite(led5, (numero >> 4) & 1);
  digitalWrite(led6, (numero >> 5) & 1);
  digitalWrite(led7, (numero >> 6) & 1);
  digitalWrite(led8, (numero >> 7) & 1);

  delay(100);

  while (Serial.available() > 0) {
      Serial.read();
    }
    Serial.println("Ingresa otro numero decimal entre 0 y 255:");
  }
}