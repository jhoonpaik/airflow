from airflow import DAG
import pendulum
import datetime

from airflow.operators.bash import BashOperator


with DAG(
    dag_id = "dags_bash_with_template",
    schedule = "10 0 * * *",
    start_date = pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_t1 = BashOperator(
        task_id='bash_t1',
        bash_command='echo "date_interval_end: {{ data_interval_end }}"'

    )

    bash_t2 = BashOperator(
        task_id='bash_t2',
        env={
            'START_DATE':'{{data_interval_start | ds }}', # DAG실행시 날짜값으로 변환. ds를 붙여야 YYYY-mm-dd 형식으로 출력 가능
            'END_DATE':'{{data_interval_end | ds }}'


        },
        bash_command= 'echo $START_DATE && echo $END_DATE' # Acmd && Bcmd: A command가 실행되면, B command도 실행
    )

    bash_t1 >> bash_t2
