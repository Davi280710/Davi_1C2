# semaforo
![semaforo foto2](semaforo2.jpg)
- Modadalidade: individual
- Entrega: Github pessoal


---

## Exercício 1
void setup()
{
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
    
}

void loop()
{
   digitalWrite(13, HIGH);
   digitalWrite(12, LOW);
   digitalWrite(11, LOW);
   digitalWrite(10, LOW);
   digitalWrite(9, HIGH);
   digitalWrite(8, LOW);
   digitalWrite(7, LOW);
   digitalWrite(6, HIGH);
  delay(5000); // Wait for 2500 millisecond(s)
   digitalWrite(13, LOW);
   digitalWrite(12, HIGH);   
   digitalWrite(11, LOW);
   digitalWrite(10, LOW);
   digitalWrite(9, HIGH);
   digitalWrite(8, LOW);
   digitalWrite(7, LOW);
   digitalWrite(6, HIGH);
  delay(2000); // Wait for 1000 millisecond(s)
   digitalWrite(13, LOW);
   digitalWrite(12, LOW);   
   digitalWrite(11, HIGH);
   digitalWrite(10, LOW);
   digitalWrite(9, HIGH);
   digitalWrite(8, HIGH);
   digitalWrite(7, LOW);
   digitalWrite(6, LOW);
  delay(6000); // Wait for 2000 millisecond(s)
   digitalWrite(13, LOW);
   digitalWrite(12, LOW);   
   digitalWrite(11, HIGH);
   digitalWrite(10, LOW);
   digitalWrite(9, HIGH);
   digitalWrite(8, LOW);
   digitalWrite(7, HIGH);
   digitalWrite(6, LOW);
  delay(2000); // Wait for 1000 millisecond(s)
  digitalWrite(13, LOW);
   digitalWrite(12, LOW);   
   digitalWrite(11, HIGH);
   digitalWrite(10, HIGH);
   digitalWrite(9, LOW);
   digitalWrite(8, LOW);
   digitalWrite(7, LOW);
   digitalWrite(6, HIGH);
  delay(6000); // Wait for 2000 millisecond(s)
   digitalWrite(10, LOW);
   digitalWrite(9, HIGH);
   delay(500);
   digitalWrite(9, LOW);
   delay(500);
   digitalWrite(9, HIGH);
   delay(500);
   digitalWrite(9, LOW);
   delay(500);
   digitalWrite(9, HIGH);
  delay(500);
