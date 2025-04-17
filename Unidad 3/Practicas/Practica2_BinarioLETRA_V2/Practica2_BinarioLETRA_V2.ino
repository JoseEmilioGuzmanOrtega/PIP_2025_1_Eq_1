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
  Serial.println("Ingresa una palabra:");
}

void loop() {
  if (Serial.available() > 0) {
    String palabra = Serial.readString();
    palabra.trim();

    if (palabra.length() > 5) {
      Serial.println("Error: Solo se permiten palabras de hasta 5 letras.");
      Serial.println("Ingresa otra palabra:");
      return;
    }
 
    for (int i = 0; i < palabra.length(); i++) {
      char caracter = palabra.charAt(i);
      char mayuscula = toupper(caracter);

      String binario = letrabinario(mayuscula);

      Serial.print("Carácter: ");
      Serial.print(mayuscula);
      Serial.print(" en binario: ");
      Serial.println(binario);

      encenderLeds(mayuscula);

      delay(1000);

      advertenciaParpadeo();

      delay(1000);

    }
    Serial.println("Ingresa otra palabra:");
  }
}

 String letrabinario(char letra) {
  String binario = "";
  for (int i = 7; i >= 0; i--) {
    binario += ((letra >> i) & 1) ? "1" : "0";
  }
  return binario;
}

void advertenciaParpadeo() {
  for (int i = 0; i < 3; i++) {
    digitalWrite(led1, 1);
    digitalWrite(led2, 1);
    digitalWrite(led3, 1);
    digitalWrite(led4, 1);
    digitalWrite(led5, 1);
    digitalWrite(led6, 1);
    digitalWrite(led7, 1);
    digitalWrite(led8, 1);
    delay(300);
    digitalWrite(led1, 0);
    digitalWrite(led2, 0);
    digitalWrite(led3, 0);
    digitalWrite(led4, 0);
    digitalWrite(led5, 0);
    digitalWrite(led6, 0);
    digitalWrite(led7, 0);
    digitalWrite(led8, 0);
    delay(300);
  }
}

void encenderLeds(char numero) {
  digitalWrite(led1, (numero >> 0) & 1);
  digitalWrite(led2, (numero >> 1) & 1);
  digitalWrite(led3, (numero >> 2) & 1);
  digitalWrite(led4, (numero >> 3) & 1);
  digitalWrite(led5, (numero >> 4) & 1);
  digitalWrite(led6, (numero >> 5) & 1);
  digitalWrite(led7, (numero >> 6) & 1);
  digitalWrite(led8, (numero >> 7) & 1);

   delay(4500);

  digitalWrite(led1, 0);
  digitalWrite(led2, 0);
  digitalWrite(led3, 0);
  digitalWrite(led4, 0);
  digitalWrite(led5, 0);
  digitalWrite(led6, 0);
  digitalWrite(led7, 0);
  digitalWrite(led8, 0);
}