/* PROGRANA PADRÃO DE ACIONAMENTO DO nRF24
 * TRANSMISSOR
 * Conexões Pinnos CE: 9, CSN: 10, SCK: 13, MO: 11, MI: 12
 * (Se ligar direto no Arduino usar VCC 3.3v, Se usar adaptador ligar no 5v)
 * 
 * Autor: Pedro Cândido do NAscimento Filho
 */

#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"

int dados[2];

RF24 radio(9,10);

const uint64_t pipe = 0xE8E8F0F0E1LL;

void setup()
{ 
  Serial.begin(9600);
  radio.begin();
  //radio.setDataRate(RF24_250KBPS);
  radio.openWritingPipe(pipe);
}

void loop()
{
  dados[0] = 6;
  dados[1] = 1;
  
  radio.write(dados, sizeof(dados) );

}

