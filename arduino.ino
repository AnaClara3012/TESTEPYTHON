// Define os pinos
const int pinoLDR = A0;        // Pino analógico conectado ao LDR
const int pinoLED = 13;        // Pino digital conectado ao LED
const int limiteLuminosidade = 600; // Limite de luminosidade (ajuste conforme ambiente)

void setup() {
  // Configura o pino do LED como saída
  pinMode(pinoLED, OUTPUT);

  // Inicia a comunicação serial para monitorar os valores do LDR
  Serial.begin(9600);
}

void loop() {
  // Lê o valor do LDR (de 0 a 1023)
  int valorLDR = analogRead(pinoLDR);

  // Exibe o valor lido no monitor serial
  Serial.print("Valor do LDR: ");
  Serial.println(valorLDR);

  // Verifica se o ambiente está escuro (valor baixo do LDR)
  if (valorLDR < limiteLuminosidade) {
    // Escuro → acende LED
    digitalWrite(pinoLED, HIGH);
    Serial.println("Ambiente escuro → LED ACESO");
  } else {
    // Claro → apaga LED
    digitalWrite(pinoLED, LOW);
    Serial.println("Ambiente claro → LED APAGADO");
  }

  delay(500); // pequeno atraso
}
