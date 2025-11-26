# metrics_publisher.py - publish custom metrics to CloudWatch (placeholder)
import boto3
cw = boto3.client('cloudwatch')
def publish(metric_name, value, namespace='DataPlatform'):
    cw.put_metric_data(Namespace=namespace, MetricData=[{{'MetricName': metric_name, 'Value': value}}])
