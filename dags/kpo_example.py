from airflow.decorators import dag, task
from airflow.configuration import conf
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)
from pendulum import datetime

YOUR_DOCKER_IMAGE = "hello-world"


@dag(
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=["KubernetesPodOperator", "TaskFlow"],
)
def kpo_example():

    kpo_task = KubernetesPodOperator(
        task_id="kpo_task",
        name="kpo-test-pod",
        image=YOUR_DOCKER_IMAGE,
        in_cluster=False,  
        kubernetes_conn_id="kube_external",
        cluster_context="demo-cluster",
        namespace="default",
        get_logs=True,
        log_events_on_failure=True,
        is_delete_operator_pod=True,
        # make sure XComs are pushed
        do_xcom_push=True,
    )
    kpo_task 
kpo_example()
