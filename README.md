PyNeoPixel
==========
A python library and arduino sketch to controll a strip of NeoPixels from a computer, raspberry pi or beaglebone via an arduino.

Arduino Sketch
--------------
The arduino sketch exposes the adafruit neopixel api over the serial line so that programs connected to the other end can controll the strip.

### Uploading the sketch
* Copy or clone the repo into the arduino sketchbook (e.g. ~/sketchbook/PyNeoPixel/PyNeoPixel.ino) 
* Use the Arduino IDE to compile and upload the sketch

Python module
-------------
There is a python module which can communicate with the Arduino sketch over serial.

#### Example

    import neopixel
    import time

    strand = neopixel.NeoPixel('/dev/ttyACM0')
    for x in range(5):
        strand.setPixelColor(x, 255, 0, 0)
        strand.show()
        time.sleep(1)
        strand.setPixelColor(x, 0, 255, 0)
        strand.show()
        time.sleep(1)
        strand.setPixelColor(x, 0, 0, 255)
        strand.show()
        time.sleep(1)
