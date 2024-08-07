from airflow.decorators import dag, task
from datetime import datetime
from airflow.providers.amazon.aws.secrets.secret_mananger import SecretsManagerBackend

@dag(
  "secret_test",
  schedule=None,
  tags=['secret'],
  catchup=False
)
def secret_dag():
  @task()
  def secret_task():
    secret_obj = SecretsManagerBackend()
    sec_client = secret_obj.client()

dag_obj = secret_dag()
