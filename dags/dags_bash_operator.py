from airflow import DAG # airflow에서 Dag 클래스를 import

import datetime
import pendulum # date 라이브러리 

from airflow.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_operator", # dag명(보통 .py 파일명과 일치시키는 걸 권장)
    schedule="0 0 * * *", # dag 실행 주기 
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False, # True로 설정시 start_date 부터 현재 날짜까지 dag가 한꺼번에 실행됨.
    # dagrun_timeout=datetime.timedelta(minutes=60), # 타임아웃 설정(60분 이상 타임걸리면 취소
    # tags=["example", "example2"], # airflow ui의 태그
    # params={"example_key": "example_value"}, # 테스크에 공통으로 줄 파라미터 지정
) as dag:
    # bash_t1: 테스크 객체명
    bash_t1 = BashOperator(
        task_id="bash_t1", # 테스크 id명도 객체명과 동일
        bash_command="echo whoami", # echo는 프린트같은 명령어
    )

    bash_t2 = BashOperator(
        task_id="bash_t2", # 테스크 id명도 객체명과 동일
        bash_command="echo $HOSTNAME", # echo는 프린트같은 명령어
    )

    bash_t1 >> bash_t2