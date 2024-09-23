from airflow.decorators import dag, task
from pendulum import datetime
import requests
from airflow.sensors.python import PythonSensor

def check_user_availability_func(**context):
    r = requests.get("https://api.github.com/users/cruseakshay")
    print(r.status_code)

    # set the condition to True if the API response was 200
    if r.status_code == 200:
        operator_return_value = r.json()['html_url']
        # pushing the link to XCom
        context["ti"].xcom_push(key="return_value", value=operator_return_value)
        return True
    else:
        operator_return_value = None
        print(f"URL returned the status code {r.status_code}")
        return False

@dag(
    start_date=datetime(2024,9,17),
    schedule=None,
    catchup=False,
    tags=["sensor", "day1"],
)
def pythonsensor_example():

    # turn any Python function into a sensor
    check_shibe_availability = PythonSensor(
        task_id="check_user_availability",
	    poke_interval=10,
        timeout=3600,
        mode="reschedule",
        python_callable=check_user_availability_func,
    )

    # click the link in the logs for the user profile :)
    @task
    def print_html_url(url):
        print(url)

    print_html_url(check_shibe_availability.output)


pythonsensor_example()