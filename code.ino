#include <Arduino.h>
#include <SPI.h>


const int AUDIO_IN = A7;


#ifndef getBit
#define getBit(sfr, bit) (_SFR_BYTE(sfr) & _BV(bit))
#endif
int threshold = 500;
int clocks_silence = 0;
bool doneRecording = 0;

bool testADCsimple(void)
{
  int i = analogRead(AUDIO_IN);
  if ( i > threshold) {
    Serial.println(i);
    return 1;
  }
  return 0;
}

void testADCfast(void)
{
  while (!getBit(ADCSRA, ADIF)) ; 
  int i = ADCL;
  i += ADCH << 8;
  bitSet(ADCSRA, ADIF); 
  bitSet(ADCSRA, ADSC); 

  Serial.println(i);
}

void setup()
{

  Serial.begin(9600);
  analogRead(AUDIO_IN); 

}

void loop()
{
  if (!doneRecording) {
    if (!testADCsimple()) {
        ++clocks_silence;
        if (clocks_silence > 25000000) {
            doneRecording = 1;
        }
    }
    else 
        clocks_silence = 0;
  } else {
    // send request
    Serial.println("DONE RECORDING")
  }
}
