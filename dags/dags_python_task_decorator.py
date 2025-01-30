from airflow import DAG
import pendulum
from airflow.decorators import task


with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    @task(task_id="python_task_1") # 테스크 데코레이터
    def print_context(some_input):
        print(some_input)

    python_task_1 = print_context('task_decorator 실행')
    # task 데코레이터 사용하면, 굳이 아래 테스크 지정안해도 됨.
