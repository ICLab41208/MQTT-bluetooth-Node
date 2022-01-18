import time
import Adafruit_DHT
import bluetooth
import sys

bd_addr = "DC:A6:32:37:EE:FC" # Server bluetooth address
port = 1 
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None :
        try:
                x = "From Wifi Temp={0:0.2f}*C  Humidity={1:0.2f}%".format(temperature, humidity)
                y = "NO.3 Humidity={1:0.2f}%".format(temperature,humidity)
                sock.send(y)
                print(y)
                time.sleep(0.5)
        except:
            try:
                print('Try to conncent again')
                sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
                sock.connect(('DC:A6:32:37:EE:FC', 1))
            except:
                pass
    else:
        print("Error!")



