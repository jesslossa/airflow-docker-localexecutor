from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'Jessica',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

# When catchup is set to true, the dag runs all the instances since the datetime set on start_date.
# When catchup is set to false, the dag only runs from the datetime it was deployed.
# If catchup is set to false but you still want to run the dag in the past dates,
# enter the shell of Airflow scheduler docker container through "docker exec -it [scheduler-container-id] bash"
# and run the command "airflow dags backfill -s [start_date] -e [end-date] [dag-id]" to get
# to run the dates you set on the interval.

with DAG(
    dag_id='basic_dag_with_catchup_backfill_false',
    default_args=default_args,
    start_date=(datetime.today() - timedelta(days=2)),
    schedule='@daily',
    # catchup=True
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a simple bash command!'
    )