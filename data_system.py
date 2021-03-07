import board
import busio
import adafruit_lps2x

import time
import os
import signal
import subprocess


class DataSystem:

    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.pressure_sensor = adafruit_lps2x.LPS25(self.i2c)
        self.subprocess = None

    def run(self):
        while True:
            print("Pressure: %.2f hPa" % self.pressure_sensor.pressure)
            print("Temperature: %.2f C" % self.pressure_sensor.temperature)
            time.sleep(2)

    # def stop(self):
    #     os.killpg(os.getpgid(self.subprocess.pid), signal.SIGTERM)


if __name__ == "__main__":
    data_system = DataSystem()
    data_system.run()
