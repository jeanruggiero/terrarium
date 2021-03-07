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
        self.subprocess = subprocess.Popen(
            ["python", __file__], stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid
        )

    def stop(self):
        os.killpg(os.getpgid(self.subprocess.pid), signal.SIGTERM)


if __name__ == "__main__":
    while True:
        print("Pressure: %.2f hPa" % lps.pressure)
        print("Temperature: %.2f C" % lps.temperature)
        time.sleep(2)