"""kinesis_stream_setup.py
Sample script showing how to create a Kinesis stream using boto3 (requires AWS credentials).
Run only in a safe environment where boto3 and AWS credentials are configured.
"""
import boto3

def create_stream(stream_name='demo-stream', shard_count=1, region='us-east-1'):
    client = boto3.client('kinesis', region_name=region)
    try:
        resp = client.create_stream(StreamName=stream_name, ShardCount=shard_count)
        print('Create stream response:', resp)
    except client.exceptions.ResourceInUseException:
        print('Stream already exists:', stream_name)

if __name__ == '__main__':
    print('This is a template. Do not run in production without reviewing.')
