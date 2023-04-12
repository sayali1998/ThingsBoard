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