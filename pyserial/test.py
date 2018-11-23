#encoding = utf-8
import serial
import serial.tools.list_ports
import time
import os
import tcpic

# a= serial.tools.list_ports.comports()

ser= serial.Serial("COM8", 115200)

print (ser)

# # display something
# display = [0x5b, 0x18, 0x18, 0x10, 0x10, 0x01, 0x00]

# words = [0xBA, 0xBC, 0xD6, 0xDD, 0xC7, 0xE5, 0xB4, 0xEF, 0xB9, 0xE2, 0xB5, 0xE7, 0xBC, 0xBC, 0xCA, 0xF5, 0xD3, 0xD0, 0xCF, 0xDE, 0xB9, 0xAB, 0xCB, 0xBE]

# # ser.write(bytes([0x5B, 0x28, 0x18, 0x10, 0x10, 0x0C, 0x00, 0xBA, 0xBC, 0xD6, 0xDD, 0xC7, 0xE5, 0xB4, 0xEF, 0xB9, 0xE2, 0xB5, 0xE7, 0xBC, 0xBC, 0xCA, 0xF5, 0xD3, 0xD0, 0xCF, 0xDE, 0xB9, 0xAB, 0xCB, 0xBE]))
# while len(words) != 0:
    
#     display.append(words.pop(0))
#     display.append(words.pop(0))
    
#     ser.write(bytes(display))

#     display[2] += 16

#     display.pop()
#     display.pop()

#     time.sleep(0.04)

# ========================================================

display = [0x5d, 0x00, 0x00, 0x40, 0x40]

#display = [0x81, 0x02, 0x00, 0x00, 0x40, 0x40, 0x01, 0x00, 0x80, 0x01]

display = display + tcpic.tcpic

ser.write(bytes(display))

time.sleep(0.5)

display = [0x5b, 0x18, 0x40, 0x10, 0x10, 0x01, 0x00]

words = [0xB1, 0xB1,
         0xBE, 0xA9,
         0xCC, 0xEC,
         0xB3, 0xBD,
         0xB9, 0xB2,
         0xB4, 0xB4,
         0xBF, 0xC6,
         0xBC, 0xBC,
         0xD3, 0xD0,
         0xCF, 0xDE,
         0xB9, 0xAB,
         0xCB, 0xBE]
   
while len(words) != 0:
    
    display.append(words.pop(0))
    display.append(words.pop(0))
    
    ser.write(bytes(display))

    display[2] += 16

    display.pop()
    display.pop()

    time.sleep(0.5)




