from airflow import DAG
import pendulum
import datetime

from airflow.operators.email import EmailOperator


with DAG(
    dag_id = "dags_email_operator",
    schedule = "0 8 1 * *", # 매월 1일 08시
    start_date = pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    send_email_task = EmailOperator(
        task_id = "send_email_task",
        to = 'grgr62@naver.com', #받을 메일
        # cc = # 참조
        subject = "Airflow Success Email", # 메일제목
        html_content="Airlfow 작업이 완료되었습니다." # 메일내용
    )