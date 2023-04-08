# GarageDoorBot

## Introduction

GarageDoorBot is a simple script for Raspbery Pi Pico W and the SB Components single-channel
Pico relay board (https://shop.sb-components.co.uk/collections/pico-hats/products/pico-single-channel-relay-hat).
Upon erceiving a ping over MQTT, the relay is closed for half a second. Useful for remote triggering of
switches. In the example in The MagPi, we used this to open and close a garage door.

## Requirements

- Rapsberry Pi Pico W with MicroPython firmware.
- MQTT Broker

## Installation

Edit `main.py` and complete the values to set up your wifi network and MQTT broker.

Copy these files to the Pico W:

- `main.py`
- `umqtt_simple.py`

## Testing

With the Pico W powered up, send a message to the MQTT topic (default: `garage/door/operator/trigger`) using your favourite client
(e.g. `mosquitto_pub`). You should hear the relay click on and off. If you do, all is working well. Now you can connect
the relay board to triggers using the NO and COM terminals. *ALWAYS* check the voltages are in safe ranges.



