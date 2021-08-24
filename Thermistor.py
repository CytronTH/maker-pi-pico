import machine
import time
import math
B = 4275; 
R0 = 100000;  
potentiometer = machine.ADC(27)     # set GP27 as analog input pin

def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    tb = convert(potentiometer.read_u16(),0,65535,0,1023)
    R = ((1023.0/tb)-1.0)*R0
    temp = (1.0/(math.log(R/100000)/B+1/298.15))-273.15
    print("%.2f" % temp)
    time.sleep(1)               # sleep for 50ms, then repeat.