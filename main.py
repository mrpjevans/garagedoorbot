import network
from machine import Pin
from machine import reset
from machine import WDT
from time import sleep

import secrets
from umqtt_simple import MQTTClient

def triggered(topic, msg):
    print("Triggered")
    relay.on()
    sleep(0.5)
    relay.off()
    client.publish(secrets.MQTT_TOPIC_ACK, b"ack")
    
def do_reset(msg="Resetting"):
    print(msg)
    wlan.active(False)
    sleep(3)
    reset()

timeout_counter = 15
relay = Pin(6, Pin.OUT)
client = MQTTClient(secrets.MQTT_CLIENT_ID, secrets.MQTT_BROKER)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

while wlan.isconnected() is False:
    print('Waiting for connection...')
    sleep(1)
    timeout_counter -=1
    if timeout_counter is 0:
        do_reset("Wifi connection unsuccessful, resetting")
        
status = wlan.ifconfig()
print('IP Address = ' + status[0])

wdt = WDT(timeout=5000)

client.connect()
print("Connected to MQTT Broker")
client.set_callback(triggered)
client.subscribe(secrets.MQTT_TOPIC)
print("Subscribed")    

while True:
    try:
        if wlan.isconnected() is False:
            do_reset("Wifi connection failed, resetting")
        print("Checking")
        client.check_msg()
        sleep(1)
        wdt.feed()
    except:
        do_reset("Unknown error, resetting")
