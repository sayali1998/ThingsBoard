# ThingsBoard
This repository contains my IoT assignment, which is a demo project on how to get started with ThingsBoard


## Documentation

[Documentation](https://thingsboard.io/docs/getting-started-guides/helloworld/?connectdevice=mqtt-linux)

## Getting Started

1. Create your account on [Thingsboard](https://thingsboard.io/)
2. Add new Devices in the device page.
![New Device](https://github.com/sayali1998/ThingsBoard/blob/main/Adding%20Device.png)
3. Configure the Device
![Device Configuration](https://github.com/sayali1998/ThingsBoard/blob/main/New%20Device.png)
4. Add MQTT Client Details
![Adding Details](https://github.com/sayali1998/ThingsBoard/blob/main/Add%20MQTT%20Client.png)
5.Install Paho.mqtt

```bash
  pip install paho-mqtt
```
6. Connect the client using python code

```python

# import paho.mqtt.client as mqtt
import random
from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo


client = TBDeviceMqttClient(host="demo.thingsboard.io", username='sayalipatil631', password='Qwerty@123456', client_id='sayalipatil631')

# Connect to ThingsBoard
client.connect()

# Sending telemetry without checking the delivery status
while True:
    telemetry = {"temperature": random.randint(-50,50), "humidity":random.randint(0,100) , "Co2 sensor" :random.randint(300,2000), "rain height": random.randint(0,50), "wind direction": random.randint(0,360), "wind Intensity": random.randint(0,100)}

    client.send_telemetry(telemetry) 
        
        # Sending telemetry and checking the delivery status (QoS = 1 by default)
    result = client.send_telemetry(telemetry)
        
        # get is a blocking call that awaits delivery status  
    success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
    # Disconnect from ThingsBoard
client.disconnect()

```
7. Create Dashboard using the telemetry tab on devices
![Dashboard](https://github.com/sayali1998/ThingsBoard/blob/main/Dashboard.png)

## Demo

https://github.com/sayali1998/ThingsBoard/blob/main/Recording.mov

## 🛠 Skills
Internet of things, Python
    
