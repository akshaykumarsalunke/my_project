from pendulum import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)
from kubernetes.client import CoreV1Api, V1Pod, models as k8s

with DAG(
    dag_id="kpod_w_resources",
    schedule="@once",
    start_date=datetime(2023, 3, 30),
) as dag:
    example_kpo = KubernetesPodOperator(
        kubernetes_conn_id="k8s_conn",
        image="hello-world",
        name="airflow-test-pod",
        task_id="task-one",
        is_delete_operator_pod=True,
        get_logs=True,
        container_resources=k8s.V1ResourceRequirements(
        requests={"cpu": "100m", "memory": "64Mi", "ephemeral-storage": "1Gi"},
        limits={"cpu": "200m", "memory": "420Mi", "ephemeral-storage": "2Gi"},
    )
    )

    example_kpo
