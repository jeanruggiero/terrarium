import boto3
from botocore.config import Config


class TimestreamClient:

    DB_NAME = 'raincloud-archive'
    TABLE_NAME = 'sensor-data'

    def __init__(self):
        session = boto3.Session()
        self.client = session.client(
            'timestream-write', config=Config(read_timeout=20, max_pool_connections=5000, retries={'max_attempts': 10})
        )

    def write_records(self, records):
        result = self.client.write_records(DatabaseName=self.DB_NAME, TableName=self.TABLE_NAME, Records=records)
        print(f"Timestream write status: {result['ResponseMetadata']['HTTPStatusCode']}")