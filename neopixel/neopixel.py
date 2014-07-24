#!/usr/bin/python
import struct
import serial
import time

class NeoPixel(object):
    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(self.port, 9600, timeout=60)
        self.command_count = 0

    def setPixelColor(self, pixel, red, green, blue):
        message = struct.pack('>BBBHBBB', ord(':'), self.command_count, ord('c'), pixel, red, green, blue)
        self.command_count += 1
        if self.command_count >=255:
            self.command_count = 0
        print(message)
        self.ser.write(message)
        response = self.ser.readline()
        print(response)

    def show(self):
        message = struct.pack('BBB', ord(':'), self.command_count, ord('s'))
        self.command_count += 1
        print(message)
        self.ser.write(message)
        response = self.ser.readline()
        print(response)


if __name__ == "__main__":
    import sys

    strand = NeoPixel(sys.argv[1])

    strand.setPixelColor(0, 255, 0, 0)
    strand.show()
    time.sleep(1)
    strand.setPixelColor(0, 0, 255, 0)
    strand.setPixelColor(1, 255, 0, 0)
    strand.show()
    time.sleep(1)
    strand.setPixelColor(0, 0, 0, 255)
    strand.setPixelColor(1, 0, 255, 0)
    strand.setPixelColor(2, 255, 0, 0)
    strand.show()
    time.sleep(1)
    strand.setPixelColor(0, 0, 0, 0)
    strand.setPixelColor(1, 0, 0, 255)
    strand.setPixelColor(2, 0, 255, 0)
    strand.show()
    time.sleep(1)
    strand.setPixelColor(0, 0, 0, 0)
    strand.setPixelColor(1, 0, 0, 0)
    strand.setPixelColor(2, 0, 0, 255)
    strand.show()
    time.sleep(1)
    strand.setPixelColor(0, 0, 0, 0)
    strand.setPixelColor(1, 0, 0, 0)
    strand.setPixelColor(2, 0, 0, 0)
    strand.show()

