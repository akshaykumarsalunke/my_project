from airflow.models.dag import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from pendulum import datetime

with DAG(
    dag_id="example_connection",
    start_date=datetime(2022, 11, 1),
    schedule=None,
    catchup=False,
    tags=["traditional", "DayOne"],
):

    call_api_simple = SimpleHttpOperator(
        task_id="call_api_simple",
        http_conn_id="random_user_api_conn",
        method="GET"
    )