"""
### Toy DAG showing the new max_active_tis_per_dag parameter.

This parameter was added in Airflow 2.6 and limits the number 
of mapped task instances within one Dagrun.
"""

from airflow.decorators import dag, task
from pendulum import datetime
import time


@dag(
    start_date=datetime(2023, 4, 18),
    schedule=None,
    catchup=False,
    tags=["dynamic"],
)
def max_active_tis_per_dagrun():
    @task()
    def return_n(n):
        time.sleep(10)
        return n

    return_n.expand(n=list(range(1000)))


max_active_tis_per_dagrun()
