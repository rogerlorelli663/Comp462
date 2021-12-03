//SendReceive.ino
#include<SPI.h>
#include<RF24.h>
// CE, CSN pins
RF24 radio(26,27);
const byte addresses[6] = "00001";
void setup(void){
  Serial.begin(9600);
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(115);
  radio.setDataRate(RF24_250KBPS);
  radio.openReadingPipe(0, addresses);
  radio.startListening();
}
void loop(void){
  if(radio.available()){
    char text[32] = "";
    radio.read(&text, sizeof(text));
    Serial.println(text);
  }
}