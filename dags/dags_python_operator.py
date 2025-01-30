from airflow import DAG
import pendulum
import datetime

from airflow.operators.python import PythonOperator

import random

with DAG(
    dag_id = "dags_python_operator",
    schedule = "30 6 * * *",
    start_date = pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    # python operator를 통해 실행할 함수
    # 랜덤으로 과일 가져오는 함수
    def select_fruit():
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        rand_int = random.randint(0,3) #0,1,2,3 중 하나 리턴
        
        return fruit[rand_int]
    

    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit
    )

    py_t1 # task 한 개만 돌림