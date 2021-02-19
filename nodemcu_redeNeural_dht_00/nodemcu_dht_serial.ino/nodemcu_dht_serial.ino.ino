#include "DHT.h"

#define DHTPIN 2    

#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);


void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  delay(2500);
 
  
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t) ){
    Serial.println("erro");
    return;
  }
  Serial.print(h);
  Serial.print(t);
  Serial.println();
}
