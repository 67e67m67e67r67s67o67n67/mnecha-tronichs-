from machine import Pin
#Import libraries

button1 = Pin(15, Pin.IN, Pin.PULL_DOWN)
led1 = Pin(18, Pin.OUT)
led2 = Pin(19, Pin.OUT)
led3 = Pin(20, Pin.OUT)
"""Setup pins
3 Seperate LEDs that will show the mode selected
1 Button for turning device on and off
"""
while True:
     while button1.value() == 1:
       led1.value(1)
       led2.value(1)
       led3.value(1)
     else:
       led1.value(0)
       led2.value(0)
       led3.value(0)

