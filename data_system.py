import board
import busio
import adafruit_lps2x

import time
import datetime
import os
import signal
import subprocess
import requests


class DataSystem:

    gateway_url = 'http://raincloud.highlift.io/data/'

    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.pressure_sensor = adafruit_lps2x.LPS25(self.i2c)

    def run(self):
        while True:
            print("Pressure: %.2f hPa" % self.pressure_sensor.pressure)
            print("Temperature: %.2f C" % self.pressure_sensor.temperature)
            requests.post(self.gateway_url + '1289/', data={
                'timestamp': datetime.datetime.now().isoformat(),
                'value': self.pressure_sensor.temperature
            })
            time.sleep(2)


if __name__ == "__main__":
    data_system = DataSystem()
    data_system.run()
