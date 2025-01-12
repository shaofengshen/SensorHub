import network
import socket
import time
import json
from machine import ADC

light = ADC(27)

def get_light_intensity():
    return int(light.read_u16() * 101 / 65536)

# 连接WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    SSID = ''
    PASSWORD = ''
    
    if not wlan.isconnected():
        print('连接到:', SSID)
        wlan.connect(SSID, PASSWORD)
        
        max_wait = 10
        while max_wait > 0:
            if wlan.isconnected():
                break
            max_wait -= 1
            print('等待连接...')
            time.sleep(1)
    
    if wlan.isconnected():
        print('WiFi已连接')
        print('网络配置:', wlan.ifconfig())
        return True
    return False

# 向指定的服务器发送数据
def send_message():
    HOST = '106.52.184.158'
    PORT = 5000
    
    try:
        s = socket.socket()
        print(f'连接到服务器 {HOST}:{PORT}...')
        s.connect((HOST, PORT))
        light_intensity = get_light_intensity()
        data = {
            "light_intensity": light_intensity,
            "timestamp": time.time()
        }
        
        # 构建HTTP POST请求
        request = f"""POST /sensor_data HTTP/1.1\r
Host: {HOST}:{PORT}\r
Content-Type: application/json\r
Content-Length: {len(json.dumps(data))}\r
\r
{json.dumps(data)}"""
        
        # 发送数据
        s.send(request.encode())
        print('数据已发送:', data)
        
        # 接收响应
        response = s.recv(1024).decode()
        print('服务器响应:', response)
        
        s.close()
        
    except Exception as e:
        print('发送失败:', e)
        
    except Exception as e:
        print('发送失败:', e)

def main():
    if connect_wifi():
        send_message()
    else:
        print('无法发送消息，WiFi未连接')

# 运行程序
main()