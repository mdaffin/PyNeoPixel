#include <Adafruit_NeoPixel.h>

#define PIN 8
Adafruit_NeoPixel strip = Adafruit_NeoPixel(3, PIN, NEO_GRB + NEO_KHZ800);

/*
\r  Start of command
\n  End of command

s  show
c  setPixelColor pixelH pixelL red green blue
b  setBrightness brightness
g  getPixelColor pixelH pixelL
n  numPixels
*/

enum Commands {
  Show = 's',
  SetColor = 'c',
  SetBrightness = 'b',
  GetColor = 'g',
  NumberPixels = 'n' 
};

void setup() {
  Serial.begin(9600);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  Serial.println("Ok");
}

bool read(char &character, long timeout = 1000) {
  long start = millis();
  while (!Serial.available()) {
    if (millis() - start > timeout) {
      return false;
    }
  }
  character = Serial.read();
  return true;
}

bool setColor() {
  char character;
  uint16_t pixel;
  uint8_t color[3];

  if (!read(character)) { return false; }
  pixel = (uint16_t) character << 8;
  if (!read(character)) { return false; }
  pixel += (uint8_t)character;
  if (!read(character)) { return false; }
  color[0] = character;
  if (!read(character)) { return false; }
  color[1] = character;
  if (!read(character)) { return false; }
  color[2] = character;
  Serial.print("  ");
  Serial.print(color[0]);
  Serial.print("  ");
  Serial.print(color[1]);
  Serial.print("  ");
  Serial.print(color[2]);
  Serial.print("  ");

  strip.setPixelColor(pixel, color[0], color[1], color[2]);
  return true;
}

void loop() {
  if (Serial.available()) {
    char character;
    if (!read(character) || character != ':') { return; }
    if (!read(character)) { return; }

    uint8_t command_index = (uint8_t)character;
    Serial.print(command_index);

    if (!read(character)) { return; }

    switch(character) {
      case Show:
        strip.show();
        Serial.println("Ok");
        break;
      case SetColor:
        if (setColor()) {
          Serial.println("Ok");
        } else {
          Serial.println("Err");
        }
        break;
      case SetBrightness:
        break;
      case GetColor:
        break;
      case NumberPixels:
        Serial.println(strip.numPixels());
        break;
    }
  }
}

