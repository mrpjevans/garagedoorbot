import network
from machine import Pin
from time import sleep

from umqtt_simple import MQTTClient

# Change these to match your settings
ssid = "your wifi network name"
password = "your wifi network password"
mqtt_broker = "the ip address of your broker"
mqtt_topic = b"garage/dooroperator"
mqtt_client_id = b"Garagedoorbot"

# Set up relay
relay = Pin(6, Pin.OUT)

# Connect to wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
max_wait = 30
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('Waiting for connection...')
    sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('Network connection failed')

status = wlan.ifconfig()
print('IP Address = ' + status[0])

def triggered(topic, msg):
    print("Triggered")
    relay(1)
    sleep(0.5)
    relay(0)
    

# Connect to MQTT
client = MQTTClient(mqtt_client_id, mqtt_broker, keepalive=3600)
client.connect()
print("Connected to MQTT Broker")

client.set_callback(triggered)

client.subscribe(mqtt_topic)
print("Subscribed")

while True:
    client.wait_msg()
