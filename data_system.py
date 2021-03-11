import time
import logging
from sensors import PressureSensor, TemperatureSensor
from timestream import TimestreamClient

logging.basicConfig(level=logging.INFO)


class DataSystem:

    gateway_url = 'http://raincloud.highlift.io/data/'

    def __init__(self):
        self.sensors = [
            PressureSensor(1, 'desk', 'test pressure sensor'),
            TemperatureSensor(2, 'desk', 'test temp sensor')
        ]

        self.timestream_client = TimestreamClient()

    def run(self):
        logging.info("[terrarium] Data system up and running.")

        # Take a sample every 5 seconds forever
        while True:
            records = [sensor.record() for sensor in self.sensors]

            # Write all records to timestream
            self.timestream_client.write_records(records)

            time.sleep(5)


if __name__ == "__main__":
    logging.info("[terrarium] Starting data system...")
    data_system = DataSystem()
    data_system.run()
