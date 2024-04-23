from airflow.models import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('stress-dag', schedule_interval=None,
        start_date=datetime(2022, 1, 1), catchup=False) as dag:
 
   stress = BashOperator(task_id='stress-dag',
                         bash_command='stress-ng --cpu 1 -v --timeout 10m'
                         )