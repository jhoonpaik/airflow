from airflow import DAG

import datetime
import pendulum # pendulum 라이브러리 사용시 타임존 설정을 매개변수로 간단히 가능(datetime은 pytz까지 불러와야 함)
from airflow.operators.bash import BashOperator 

with DAG(
    dag_id="dags_bash_operator", # dag_id: 화면에서 보이는 dag명(python 파일명과 관계x. but 일반적으로 dag파일명과 py파일명 일치시키는게 표준)
    schedule="0 0 * * *", # cron 주기
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),# Asia/Seoul 기준 2011-01-01 부터 스타트
    
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60), # 타임아웃 설정(DAG 60분이상 돌면 실패로 설정)
    # tags=["example", "example2"], # dag별 tag 지정
    # params={"example_key": "example_value"}, # 밑의 task들에게 공통적으로 입력할 파라미터
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


"""
catchup: dag 실행 시작 후, 미실행된 dag 수행 여부(T: 수행)
ex. start_date가 2021-01-01 이고, 현재 날짜가 2021-01-04 면,
True: 01-01 부터 01-04 까지 dag 실행을 차례대로 수행 후, 자정에(`0 0 * * *`) 01-05 dag 실행
False: 01-01 부터 01-04 까지 실행을 스킵하고, 자정에(`0 0 * * *`) 01-05 dag 실행
꼭 해야되는 경우가 아니면 catchup=F 권장(다른 이슈가 발생할 수도 있음)

"""