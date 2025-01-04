from machine import Pin, I2C
import utime
from dht11 import DHT11
i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=100000)

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128,32, i2c)

# 初始化温湿度引脚
pin = Pin(22, Pin.OUT)
# 初始化温湿度库
dht11 = DHT11(pin)

while True:
    temperature = dht11.temperature
    humidity = dht11.humidity
    # 打印数据
    print("temperature=%dC, humidity=%d%%" % (temperature, humidity))
    
    # 格式化数据为字符串格式
    str_temperature = "tem=%dC"%(temperature)
    str_humidity = "hum=%d%%"%(humidity)
    
    # oled 显示数据
    oled.fill(0x0)
    oled.text(str_temperature, 0, 0)
    oled.text(str_humidity, 0, 10)
    oled.show()
    
    utime.sleep(30)