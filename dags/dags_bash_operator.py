from airflow import DAG

import datetime
import pendulum
from airflow.operators.bash import BashOperator 

with DAG(
    dag_id="dags_bash_operator",
    # dag_id: 화면에서 보이는 dag명(python 파일명과 관계x. but 일반적으로 dag파일명과 py파일명 일치시키는게 표준)
    schedule="0 0 * * *", # cron 주기
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), # Asia/Seoul 기준 2011-01-01 부터 스타트
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag:
    bash_t1 = BashOperator( # task 객체명
        task_id="bash_t1", # task명도 task객체명과 동일하게 권장
        bash_command="echo whoami", # 쉘에서 whoami 출력(echo)
    )
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME", # hostname 환경변수 출력
    )

    # task 수행순서
    bash_t1 >> bash_t2