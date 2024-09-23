from airflow.decorators import dag, task
from airflow.models import Variable
from pendulum import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator

POSTGRES_CONN_ID = "postgres_default"


@dag(start_date=datetime(2024,9,17), schedule=None, catchup=False, tags=["connection", "variable", "day1"])
def example_connection_variable():
    
    table_to_query = Variable.get('table')

    query_table = PostgresOperator(
        task_id="query_table",
        postgres_conn_id="postgres_default",
        sql=f"SELECT * FROM {table_to_query};",
        show_return_value_in_logs=True,
    )

    query_table

example_connection_variable()