"""Control System Server to respond to device commands."""

from flask import Flask
from gpiozero import LED

app = Flask(__name__)

led = LED(4)


@app.route('/control/led/on')
def led_on():
    led.on()
    return 'Led is on'


@app.route('/control/led/off')
def led_on():
    led.on()
    return 'Led is on'

