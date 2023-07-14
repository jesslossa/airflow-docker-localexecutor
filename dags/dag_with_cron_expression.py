from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'Jessica',
    'retries': 5,
    'retry_delay': timedelta(minutes=5) 
}

with DAG(
    default_args=default_args,
    dag_id="dag_with_cron_expression",
    start_date=(datetime.today() - timedelta(days=2)),
    schedule='0 0 * * *' # cron for daily
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo dag with cron expression!"
    )
    task1