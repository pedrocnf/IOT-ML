#include "DHT.h"

#define DHTPIN D4    
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);  


void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float temperatura = dht.readTemperature();
  Serial.println(temperatura); 
  delay(2000); 
}
