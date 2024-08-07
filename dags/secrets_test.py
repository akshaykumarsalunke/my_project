from airflow.decorators import dag, task
from datetime import datetime
from airflow.providers.amazon.aws.secrets.secrets_manager import SecretsManagerBackend

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

  t1 = secret_task()

dag_obj = secret_dag()
