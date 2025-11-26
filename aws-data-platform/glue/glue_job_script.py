# glue_job_script.py
# Example AWS Glue ETL job script (PySpark compatible)
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from Glue Catalog (example)
datasource = glueContext.create_dynamic_frame.from_catalog(database = "default", table_name = "raw_table")
df = datasource.toDF()
# Transform
df = df.withColumn('processed_at', df['some_col'])  # placeholder
# Write back to S3 / catalog
df.write.mode('overwrite').parquet('s3://your-bucket/processed/')

job.commit()
