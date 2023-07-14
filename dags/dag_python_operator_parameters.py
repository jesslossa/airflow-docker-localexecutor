from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'Jessica',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(name, age):
    print(f"Hello World from {name}! I am {age} years old.")


def get_name():
    return "Jessica"


with DAG(
    default_args=default_args,
    dag_id='dag_with_python_operator_parameters',
    description='Dag with parameters',
    start_date=(datetime.today() - timedelta(days=2)),
    schedule='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'name': 'Jessica', 'age': 27}
    )

    task2 = PythonOperator(
       task_id='get_name',
       python_callable=get_name
    )