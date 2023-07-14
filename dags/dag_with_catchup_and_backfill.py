from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'Jessica',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

# When catchup is set to true, the dag runs all the instances since the datetime set on start_date
# When catchup is set to false, the dag runs only from the datetime it was deployed
with DAG(
    dag_id='basic_dag_with_catchup_backfill_false',
    default_args=default_args,
    start_date=(datetime.today() - timedelta(days=2)),
    schedule_interval='@daily',
    # catchup=True
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a simple bash command!'
    )