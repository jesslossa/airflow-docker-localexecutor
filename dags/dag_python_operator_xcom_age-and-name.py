from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'Jessica',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello World from {last_name}, {first_name}! I am {age} years old.")


def get_name(ti):
    ti.xcom_push(key='first_name', value='Jessica')
    ti.xcom_push(key='last_name', value='Silva')


def get_age(ti):
    ti.xcom_push(key='age', value=27)


with DAG(
    default_args=default_args,
    dag_id='dag_with_python_operator_parameters-xcom_age-and-name',
    description='Dag with parameters',
    start_date=datetime(2023, 7, 12),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )

    task2 = PythonOperator(
       task_id='get_name',
       python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1