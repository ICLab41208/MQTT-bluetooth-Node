# MQTT-bluetooth-Node
透過藍芽接收資訊再上傳到MQTT上



分為broker端與Node端兩段程式碼
broker端主要為透過藍芽通訊接收來自Node端的資料後再自行到MQTT上 IP預設為127.0.0.1(本身為MQTT Server) 也可自行更改broker IP 位址
Node端主要為使用dht11溫溼度感測器，再將數值藉由Bluetooth通訊傳輸至broker端

