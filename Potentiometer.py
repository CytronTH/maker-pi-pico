import machine
import time

potentiometer = machine.ADC(27)     # กำหนดใช้งาน Pin ที่ 27 เป็น Analog Output

def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    x = potentiometer.read_u16()
    y = convert(x,272,65535,0,28)
    for z in range(y):
        machine.Pin(z).value(1)
    time.sleep_ms(50)              