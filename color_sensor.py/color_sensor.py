import ws2812b
import utime
from machine import Pin, I2C
from color import color
from ssd1306 import SSD1306_I2C

# 显示屏
oled_i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=100000)
# 光传感器
color_sensor_i2c = I2C(1, scl=Pin(19), sda=Pin(18), freq=100000)

# 初始化
Color = color(color_sensor_i2c)
oled = SSD1306_I2C(128, 32, oled_i2c)

ring_pin = 17  # 灯环引脚
numpix = 8  # RGB 灯的数量
strip = ws2812b.ws2812b(numpix, 0, ring_pin)

# 关闭所有灯
strip.fill(0, 0, 0)
strip.show()

utime.sleep(0.1)

while True:
    Colors = Color.GetColor()  # 获取颜色识别传感器的数据
    r = Colors[0]
    g = Colors[1]
    b = Colors[2]
    
    str_r = "Red is %d"%(r)
    str_g = "Green is %d"%(g)
    str_b = "Blue is %d"%(b)
    strip.fill(r, g, b)    # 设置颜色
    strip.show()
    oled.fill(0x0)
    oled.text(str_r, 0, 0)
    oled.text(str_g, 0, 10)
    oled.text(str_b, 0, 20)
    oled.show()
    utime.sleep(30)

