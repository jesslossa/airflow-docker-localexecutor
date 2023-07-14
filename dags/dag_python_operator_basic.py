from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'Jessica',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet():
    print("Hey, Basic Hello World!")


with DAG(
    default_args=default_args,
    dag_id='dag_python_operator_basic',
    description='Basic dag using PythonOperator',
    start_date=(datetime.today() - timedelta(days=2)),
    schedule='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )