from datetime import datetime, timedelta

from airflow.decorators import dag, task


default_args = {
    'owner': 'Jessica',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='basic_dag_with_taskflow_api', 
     description='Basic dag using taskflow api',
     default_args=default_args, 
     start_date=(datetime.today() - timedelta(days=2)),
     schedule='@daily')
def hello_world_etl():

    @task()
    def get_name():
        return 'Jessica'

    @task()
    def get_age():
        return 27

    @task()
    def greet(name, age):
        print(f"Hello World! My name is {name} "
              f"and I am {age} years old!")
    
    name = get_name()
    age = get_age()
    greet(name=name, age=age)

greet_dag = hello_world_etl()
