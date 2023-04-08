# GarageDoorBot v2

## Introduction

GarageDoorBot is a simple script for Raspbery Pi Pico W and the SB Components single-channel
Pico relay board (https://shop.sb-components.co.uk/collections/pico-hats/products/pico-single-channel-relay-hat).
Upon erceiving a ping over MQTT, the relay is closed for half a second. Useful for remote triggering of
switches. In the example in The MagPi, we used this to open and close a garage door.

## Improvements over v1

- Sensitive data moved to `secrets.py`
- More resiliant to failure
- Acknowledgment MQTT message sent by Pico W

## Requirements

- Rapsberry Pi Pico W with MicroPython firmware.
- MQTT Broker

## Installation

Make a copy of `example_secrets.py` called `secrets.py` and replace the values
contained within < >. (You can also change the other values to suit if you wish)

Copy these files to the Pico W:

- `main.py`
- `umqtt_simple.py`
- `secrets.py`

## Testing

With the Pico W powered up, send a message to the MQTT topic (default: `garage/door/operator/trigger`) using your favourite client
(e.g. `mosquitto_pub`). You should hear the relay click on and off. If you do, all is working well. Additionally you
should see an 'ack' message arrive at `garage/door/operator/ack` which is the Pico W confirming it heard you. Now you can connect
the relay board to triggers using the NO and COM terminals. *ALWAYS* check the voltages are in safe ranges.



