#encoding = utf-8
import serial
import serial.tools.list_ports
import os

# a= serial.tools.list_ports.comports()

ser= serial.Serial("COM8", 115200)

print (ser)

ser.write(bytes([0x5B, 0x28, 0x18, 0x10, 0x10, 0x0C, 0x00, 0xBA, 0xBC, 0xD6, 0xDD, 0xC7, 0xE5, 0xB4, 0xEF, 0xB9, 0xE2, 0xB5, 0xE7, 0xBC, 0xBC, 0xCA, 0xF5, 0xD3, 0xD0, 0xCF, 0xDE, 0xB9, 0xAB, 0xCB, 0xBE]))
 
