from machine import ADC
import utime

light = ADC(27)

def get_value():
    return int(light.read_u16() * 101 / 65536)

while True:
    value = get_value()
    print(get_value())
    utime.sleep(.1)