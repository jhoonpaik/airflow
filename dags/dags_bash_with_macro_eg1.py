"""
예시1 실습: dags_bash_with_macro_eg1.py
매월 말일 수행되는 Dag에서
변수 START_DATE: 전월 말일,
변수 END_DATE: 어제로 env 셋팅하기

"""

from airflow import DAG
import pendulum

from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_macro_eg1",
    schedule="10 0 L * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    # START_DATE: 전월 말일, END_DATE: 1일 전
    bash_task_1 = BashOperator(
        task_id="bash_task_1",
        env={'START_DATE': '{{ data_interval_start.in_timezone("Asia/Seoul") | ds}}', # 날짜변수 default tz는 utc이므로 kor tz로 설정
             'END_DATE':'{{ (data_interval_end.in_timezone("Asia/Seoul") - macro.dateuil.relativedelta.relativedelta(days=1)) | ds}}'
        },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )