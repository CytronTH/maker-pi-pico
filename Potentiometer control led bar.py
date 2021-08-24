import machine
import utime
yold = [0]
j=0
k=0
potentiometer = machine.ADC(27)     # กำหนดใช้งาน Pin ที่ 27 เป็น Analog Output

def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
yold[0] = 0
while True:
    x = potentiometer.read_u16()
    y = convert(x,0,65535,0,27)
    if y < yold[0]:
        j = yold[0] - y
        k = yold[0] - j
        for q in range(k,yold[0]):
            machine.Pin(q,machine.Pin.OUT)
            machine.Pin(q).value(0)
    else:
        for z in range(y):
            machine.Pin(z,machine.Pin.OUT)
            machine.Pin(z).value(1)
    utime.sleep(0.1)
    yold.pop()
    yold.append(y)