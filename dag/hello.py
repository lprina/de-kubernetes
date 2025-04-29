from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'thesimpledata',
    'start_date': datetime(year=2025, month=4, day=29),
    'catchup': False
}

dag = DAG(
    dag_id='hello_world',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)

t1 = BashOperator(
    task_id='hello_world',
    bash_command='echo "Hello Luiz"',
    dag=dag
)

t2 = BashOperator(
    task_id='hello_fernando',
    bash_command='echo "Hello Fernando"',
    dag=dag
)

t1 >> t2
