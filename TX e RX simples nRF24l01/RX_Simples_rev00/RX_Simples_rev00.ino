/* PROGRANA PADRÃO DE ACIONAMENTO DO nRF24
 * RECEPTOR
 * Conexões Pinnos CE: 9, CSN: 10, SCK: 13, MO: 11, MI: 12
 * (Se ligar direto no Arduino usar VCC 3.3v, Se usar adaptador ligar no 5v)
 * 
 * Autor: Pedro Cândido do NAscimento Filho
 */

#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"

int dados[2]; //Vetor de dados a trasmitir, pode ser mudado o tamanho

const uint64_t pipe = 0xE8E8F0F0E1LL; //Pipe de comunicação

RF24 radio(9,10); //Configuração do CE e do CSN

void setup()
{
  Serial.begin(9600);
  radio.begin();
  //radio.setDataRate(RF24_250KBPS);
  radio.openReadingPipe(1,pipe);
  radio.startListening();
}

void loop()
{
  if ( radio.available() )
  {
      radio.read(dados, sizeof(dados) );
      Serial.println(dados[0]);
      Serial.println(dados[1]); 
  }
  else
  {
    Serial.println("Rádio não disponível");
  }
  delay(1000);
}
