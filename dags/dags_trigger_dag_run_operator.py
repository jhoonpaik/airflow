
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
import pendulum

with DAG(
    dag_id='dags_trigger_dag_run_operator',
    start_date=pendulum.datetime(2023, 4, 1, tz='Asia/Seoul'),
    schedule='30 9 * * *',
    catchup=False
) as dag:
    start_task=BashOperator(
        task_id='start_task',
        bash_command='echo "start!"',
    )

    trigger_dag_task = TriggerDagRunOperator(
        task_id='trigger_dag_task', # task_id(필수)
        trigger_dag_id='dags_python_operator', # 실행시킬 dag 설정(필수)
        trigger_run_id=None, # 수행 방식 지정(Schedule, manual(trigger 실행), Backfill)
        execution_date='{{ data_interval_start }}', # manual_{{ execution_date }} 로 수행
        reset_dag_run=True, # 이미 실행이력이 있는 dag를 run할 것인지 여부
        wait_for_completion=False,
        poke_interval=60,
        allowed_states=['success'],
        failed_states=None
        )

    start_task >> trigger_dag_task
