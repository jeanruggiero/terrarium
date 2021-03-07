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
        self.sensors = [
            PressureSensor(1, 'desk', 'test pressure sensor'),
            TemperatureSensor(2, 'desk', 'test temp sensor')
        ]

    def run(self):
        while True:
            for sensor in self.sensors:
                print(sensor.status())
                sensor.post(self.gateway_url)
            time.sleep(5)


class Sensor:

    def __init__(self, sensor_id, type, units, sample_rate, location, description):
        self.sensor_id = sensor_id
        self.type = type
        self.units = units
        self.sample_rate = sample_rate
        self.location = location
        self.description = description

    def sample(self):
        raise NotImplementedError

    def post(self, url):
        requests.post(f"{url}{self.sensor_id}/", data={
            'timestamp': datetime.datetime.now().isoformat(),
            'value': self.sample()
        })

    def status(self):
        return f"{self.type}: {self.sample():.2f} {self.units}"


class PressureSensor(Sensor):

    def __init__(self, sensor_id, location, description):
        super().__init__(sensor_id, 'pressure', 'HPa', 0.5, location, description)
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_lps2x.LPS25(self.i2c)

    def sample(self):
        return self.sensor.pressure


class TemperatureSensor(Sensor):

    def __init__(self, sensor_id, location, description):
        super().__init__(sensor_id, 'temperature', 'degC', 0.5, location, description)
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_lps2x.LPS25(self.i2c)

    def sample(self):
        return self.sensor.temperature



if __name__ == "__main__":
    data_system = DataSystem()
    data_system.run()
