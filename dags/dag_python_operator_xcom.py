from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'Jessica',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(age, ti):
    name = ti.xcom_pull(task_ids='get_name')
    print(f"Hello World from {name}! I am {age} years old.")


def get_name():
    return "Jessica"


with DAG(
    default_args=default_args,
    dag_id='dag_with_python_operator_parameters-xcom_test',
    description='Dag with parameters - v1',
    start_date=(datetime.today() - timedelta(days=2)),
    schedule='@daily'
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