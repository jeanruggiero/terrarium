import time
from sensors import PressureSensor, TemperatureSensor
from timestream import TimestreamClient

class DataSystem:

    gateway_url = 'http://raincloud.highlift.io/data/'

    def __init__(self):
        self.sensors = [
            PressureSensor(1, 'desk', 'test pressure sensor'),
            TemperatureSensor(2, 'desk', 'test temp sensor')
        ]

        self.timestream_client = TimestreamClient()

    def run(self):
        while True:
            records = [sensor.record() for sensor in self.sensors]
            self.timestream_client.write_records(records)

            print(records)

            time.sleep(5)


if __name__ == "__main__":
    data_system = DataSystem()
    data_system.run()
