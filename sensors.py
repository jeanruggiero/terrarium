import board
import busio
import adafruit_si7021
import time


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

    def record(self):

        return {
            'MeasureName': str(self.sensor_id),
            'MeasureValue': f"{self.sample():.4f}",
            'MeasureValueType': 'DOUBLE',
            'Time': self.time(),
            'Dimensions': [{'Name': 'type', 'Value': self.type}]
        }

    def status(self):
        return f"{self.type}: {self.sample():.2f} {self.units}"

    @staticmethod
    def time():
        return str(round(time.time() * 1000))


class HumiditySensor(Sensor):

    def __init__(self, sensor_id, location, description):
        super().__init__(sensor_id, 'humidity', '%', 0.5, location, description)
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_si7021.SI7021(self.i2c)

    def sample(self):
        return self.sensor.relative_humidity


class TemperatureSensor(Sensor):

    def __init__(self, sensor_id, location, description):
        super().__init__(sensor_id, 'temperature', 'degC', 0.5, location, description)
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_si7021.SI7021(self.i2c)

    def sample(self):
        return self.sensor.temperature
