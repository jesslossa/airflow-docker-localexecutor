from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'Jessica',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(age, ti):
    first_name = ti.xcom_pull(task_ids='get_name', key ='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key ='last_name')
    print(f"Hello World from {last_name}, {first_name}! I am {age} years old.")


def get_name(ti):
    ti.xcom_push(key='first_name', value='Jessica')
    ti.xcom_push(key='last_name', value='Silva')

with DAG(
    default_args=default_args,
    dag_id='dag_with_python_operator_parameters-xcom_first_last_name',
    description='Dag with parameters',
    start_date=datetime(2023, 7, 12),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'age': 27}
    )

    task2 = PythonOperator(
       task_id='get_name',
       python_callable=get_name
    )

    task2 >> task1