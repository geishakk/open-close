# Write your code here :-)
from machine import Pin
import time

p2 =Pin(2,Pin.OUT)
p4 =Pin(4,Pin.OUT)
p15 =Pin(15,Pin.OUT)
p17 =Pin(17,Pin.OUT)
p5 =Pin(5,Pin.OUT)
p18 =Pin(18,Pin.OUT)
p19 =Pin(19,Pin.OUT)
p21 =Pin(21,Pin.OUT)

REED_SWITCH_PIN = 21  # Change to your chosen GPIO pin

# Set up the reed switch as an input with a pull-up resistor
reed_switch = Pin(REED_SWITCH_PIN, Pin.IN, Pin.PULL_UP)

while True:
    if reed_switch.value() == 0:  # Reed switch closed (magnet near)
        p2.value(1)
        time.sleep(0.5)
        p4.value(1)
        time.sleep(0.5)
        p15.value(1)
        print("<3")
    else:  # Reed switch open (magnet far)
        p2.value(0)
        p4.value(0)
        p15.value(0)
        print("bring magnet closer")

    time.sleep(2)  # Delay to avoid spamming
