import bluetooth
import threading
import paho.mqtt.client as mqtt
import time
import re
from bt_proximity import BluetoothRSSI
import sys
import socket
client = mqtt.Client()
client.username_pw_set("ives","12345")
client.connect("127.0.0.1", 1883, 60)
client.loop_start()
client.reconnect_delay_set()
server_socket=None
count = 0
def serveSocket(sock,info):
    btrssi = BluetoothRSSI(addr=info)
    while True:         
        try:
            receive=sock.recv(1024).decode('utf-8');            
            h = (f'{receive}' + '    ' +'rssi :%s' %btrssi.get_rssi()).encode()
            h1 = (f'{receive}').encode()
            print(h)
            client.publish('pi/bluetooth/%s '%str(info), payload=h1 , qos=0, retain=False)
        except  :     
               client.publish('pi/bluetooth/%s'%str(info), payload='{"status": "Off"}', qos=0, retain=False)
               sock_client.close(info[0])
               client.disconnect()
               client.loop_stop()
               
server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM);
server_socket.bind(("",1))
server_socket.listen(10);


while True:
    try:
        sock,info=server_socket.accept();
        client.loop_start()
        print(str(info[0])+'   Connected!');
        client.publish('pi/bluetooth/%s '%str(info[0]), payload='{"status": "Online"}' , qos=0, retain=False)
        t=threading.Thread(target=serveSocket,args=(sock,info[0]))
        t.setDaemon(True)
        t.start();
    except KeyboardInterrupt:
        sock.close()

        
        
