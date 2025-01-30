from airflow import DAG
import pendulum
import datetime

from airflow.operators.python import PythonOperator

# from plugins.common.common_func import get_sftp
from common.common_func import get_sftp

# 로컬에서는 plugins.common.common_func이 에러 안뜨고
# 컨테이너에서는 common.common_func가 에러 안뜸
# 컨테이너에서는 plugins까지 path로 잡고있기 때문임.
# 에러안뜨게 하려면 .env에 WORKSPACE_FOLDER, PYTHONPATH 추가
# .env는 굳이 커밋할필요 없으므로 .gitignore에 추가




with DAG(
    dag_id = "dags_python_import_func",
    schedule = "30 6 * * *",
    start_date = pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    task_get_sftp = PythonOperator(
        task_id='task_get_sftp',
        python_callable=get_sftp
    )
