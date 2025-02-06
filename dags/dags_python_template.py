from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
from airflow.decorators import task


with DAG(
    dag_id="dags_python_template",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2023, 3, 10, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    

# 1\. op_kwargs에 직접 jinja 템플릿 변수를 주고 이걸 함수로 꺼내쓰는 법

    def python_function1(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)

    python_t1 = PythonOperator(
        task_id='python_t1',
        python_callable=python_function1,
        op_kwargs={'start_date':'{{date_interval_Start | ds}}', 'end_date':'{{data_interval_end | ds}}'}
    )

# 2\. kwargs 에서 딕셔너리 형태로 꺼내쓰는 법
    @task(task_id='python_t2')
    def python_function2(**kwargs):
        print(kwargs)
        print('ds:' + kwargs['ds'])
        print('ts:' + kwargs['ts'])
        print('data_interval_start:' + str(kwargs['data_interval_start']))
        print('data_interval_end:' + str(kwargs['data_interval_end']))
        print('task_instance:' + str(kwargs['ti']))

    python_t1 >> python_function2()

