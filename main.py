# main.py -- put your code here!
import pyb   # importing the board
# move servo based on the movement of the board
from pyb import Servo
accel = pyb.Accel()     # assigning the sensor to act as movement detector…
ss = Servo(1) # servo on position 1 (X1, VIN, GND)
while True:     # while loop, looping while switch is not pressed…
    if accel.x() > 5:
        ss.angle(90)
    elif accel.x() < -5:
        ss.angle(-90)
    elif accel.x() == 0:
        ss.angle(0)
