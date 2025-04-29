from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'thesimpledata'
    'start_date': datetime(year:2025, month:4, day:29),
    'catchup': False
}

dag = DAG(
    dag_id: 'hello_world',
    default_args = default_args,
    schedules=timedelta(days=1)
)

t1 = BashOperator(
    task_id='hello_world',
    bash_command = 'echo "Hellow Luiz"
    dag = dag
)

t2 = BashOperator(
    task_id='hello_fernandp',
    bash_command = 'echo "Hellow Fernando"
    dag = dag
)

t1 >> t2