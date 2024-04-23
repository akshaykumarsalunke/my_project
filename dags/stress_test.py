from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from datetime import datetime

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3},
    tags=["example"],
)
def stress_dag():

   stress = BashOperator(task_id='stress-dag',
                         bash_command='stress-ng --cpu 1 -v --timeout 10m'
                         )
   
# Instantiate the DAG
stress_dag()