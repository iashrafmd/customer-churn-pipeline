from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "ashraf",
    "retries": 1
}

with DAG(
    dag_id="customer_churn_etl",
    default_args=default_args,
    description="Simple daily export and upload pipeline",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    export_task = BashOperator(
        task_id="export_data",
        bash_command="python /opt/airflow/scripts/export_data.py"
    )

    upload_task = BashOperator(
        task_id="upload_to_s3",
        bash_command="python /opt/airflow/scripts/upload_to_s3.py"
    )

    export_task >> upload_task