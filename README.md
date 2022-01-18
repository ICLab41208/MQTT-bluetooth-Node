# MQTT-bluetooth-Node
透過藍芽接收資訊再上傳到MQTT上



分為broker端與Node端兩段程式碼
broker端主要為透過藍芽通訊接收來自Node端的資料後再自行到MQTT上 IP預設為127.0.0.1(本身為MQTT Server) 也可自行更改broker IP 位址
Node端主要為使用dht11溫溼度感測器，再將數值藉由Bluetooth通訊傳輸至broker端

先更新系統
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-dev python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel


安裝依賴件↓  broker 與Node端階需要安裝

1.安裝Mosquitto (MQTT)

sudo apt-get install mosquitto mosquitto-clients

2.安裝 bt-proximity 顯示RSSI訊號強度

sudo pip install bt-proximity

3.安裝藍芽依賴套件

sudo apt-get install Python-dev

sudo apt-get install libbluetooth-dev

sudo pip3 install pybluez

Node端 額外安裝 依賴件↓  #DHT11感測器
1.sudo pip3 install Adafruit_DHT

安裝完成後，Node端 程式內需要修改 broker端的bluetooth address 

