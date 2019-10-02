int led = 7;
int valor;

void setup() {                
  Serial.begin(9600);
  pinMode(led, OUTPUT);   
  
}

void loop() {
  if(Serial.available())
  {
    valor = Serial.read();
    if(valor == '1')
    {
      digitalWrite(led, HIGH);
    }
    if(valor == '2')
    {
      digitalWrite(led, LOW);
    }
  
  }
}
