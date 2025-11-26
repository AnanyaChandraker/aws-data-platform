# mwaa_dag.py - Example Airflow DAG for MWAA
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {{
    'owner': 'data-platform',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}}

def dummy_task(**kwargs):
    print('Run task')

with DAG('sample_etl_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    run = PythonOperator(task_id='run_etl', python_callable=dummy_task)
