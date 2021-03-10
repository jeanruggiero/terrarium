import os
import boto3
from botocore.config import Config


class TimestreamClient:

    DB_NAME = 'raincloud-archive'
    TABLE_NAME = 'sensor-data'

    def __init__(self):
        session = boto3.Session(
            aws_access_key_id=os.environ.get('TIMESTREAM_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('TIMESTREAM_SECRET_ACCESS_KEY')
        )

        self.client = session.client(
            'timestream-write', config=Config(read_timeout=20, max_pool_connections=5000, retries={'max_attempts': 10},
                                              region_name="us-west-2")
        )

    def write_records(self, records):
        self.client.write_records(DatabaseName=self.DB_NAME, TableName=self.TABLE_NAME, Records=records)