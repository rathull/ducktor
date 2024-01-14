#include <Arduino.h>
#include <SPI.h>
#include <ESP32Time.h>

const int AUDIO_IN = 35;
const int THRESHOLD = 2000;
ESP32Time rtc(3600);
// #ifndef getBit
// #define getBit(sfr, bit) (_SFR_BYTE(sfr) & _BV(bit))
// #endif
bool is_recording, is_done_recording;

bool testADCsimple(void)
{
  int i = analogRead(AUDIO_IN);
  if (i > THRESHOLD) is_recording = true;
  if (is_recording) Serial.println(i);
  return i > THRESHOLD;
}

void setup()
{
  Serial.begin(9600);
  analogRead(AUDIO_IN); 
  rtc.setTime(1, 0, 0, 1, 1, 2023);
  above_threshold = false;
  is_recording = false;
  is_done_recording = false;
}

void loop()
{
  if (is_done_recording) return;
  if (testADCsimple()) {
    rtc.setTime(0, 0, 0, 1, 1, 2023);
    return;
  }

  // if !above_threshold
  if (rtc.getSecond() == 0) {
    // Set to 1 second
    rtc.setTime(1, 0, 0, 1, 1, 2023);
    return;
  }
  if (rtc.getSecond() >= 4) {
    // Send request
    Serial.println("SEND HHTP REQUEST TO SERVER HERE");
    is_done_recording = true;
  }
}