# dq_runner.py - simple Data Quality runner using PySpark
from pyspark.sql import SparkSession

def run_dq(input_path):
    spark = SparkSession.builder.appName('dq_runner').getOrCreate()
    df = spark.read.parquet(input_path)
    # Example rule: no null ids
    null_count = df.filter(df.id.isNull()).count()
    if null_count > 0:
        raise Exception('DQ failed: null ids found')
    print('DQ passed')
    spark.stop()

if __name__ == '__main__':
    print('This is a template DQ runner.')
