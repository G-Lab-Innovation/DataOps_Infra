from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.operators.s3 import S3CopyObjectOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 14),
    'email': ['atul@glabinnovation.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    's3_copy_objects',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
) as dag:

    start = DummyOperator(task_id='start')

    copy_files = S3CopyObjectOperator(
        task_id='copy_object',
        aws_conn_id='my_aws',
        source_bucket_name='airflowtest-bucket-1',
        source_bucket_key='ds_salaries.csv',
        dest_bucket_name='airflow-test-bucket-2',
        dest_bucket_key='ds_copy.csv'
    )

    end = DummyOperator(task_id='end')

    start >> copy_files >> end
