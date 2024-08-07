from datetime import datetime

from airflow import DAG
from airflow.hooks.base import BaseHook
from airflow.models import Variable
from airflow.operators.python import PythonOperator


def print_var():
    # my_var = Variable.get("my_var")
    # print(f'My variable is: {my_var}')

    conn = BaseHook.get_connection(conn_id="my_db")
    print(conn.get_uri())


with DAG('example_secrets_dag', start_date=datetime(2022, 1, 1), schedule=None) as dag:

  test_task = PythonOperator(
      task_id='test-task',
      python_callable=print_var
)
