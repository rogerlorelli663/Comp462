//SendReceive.ino
#include<SPI.h>
#include <nRF24L01.h>
#include<RF24.h>
// CE, CSN pins
RF24 radio(7,8);

const byte addresses[6] = "00001";
void setup(void){
  Serial.begin(9600);
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(115);
  radio.setDataRate(RF24_250KBPS);
  radio.openWritingPipe(addresses); // 00001
  radio.stopListening();
}
void loop(void){
  const char text[] = "Hello World";
  radio.write(&text, sizeof(text));
  Serial.println("Sent");
  delay(1000);
}