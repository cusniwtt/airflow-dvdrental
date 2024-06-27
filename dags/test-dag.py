from airflow.decorators import dag, task, task_group
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

@dag(
    dag_id='test-dag',
    start_date=days_ago(1),
    schedule_interval='50 * * * *',
    catchup=False,
    tags=['dps-dashboard']
)
def test_dag():
    upstream = EmptyOperator(task_id="start")

    downstream = EmptyOperator(task_id="end")

    upstream >> downstream

test_dag()



