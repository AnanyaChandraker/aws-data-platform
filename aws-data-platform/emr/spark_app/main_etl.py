"""main_etl.py
PySpark ETL job suitable for EMR Spark submit.
This script reads JSON lines from S3, performs simple transforms, and writes Parquet.
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

def run():
    spark = SparkSession.builder.appName('sample_etl').getOrCreate()
    input_path = 's3://your-bucket/raw/*'
    output_path = 's3://your-bucket/processed/'
    df = spark.read.json(input_path)
    df = df.withColumn('_ingested_at', current_timestamp())
    df.write.mode('overwrite').parquet(output_path)
    spark.stop()

if __name__ == '__main__':
    run()
