from airflow.decorators import dag, task, task_group
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

import polars as pl
import subprocess
import logging

@dag(
    dag_id='test-dag',
    start_date=days_ago(1),
    schedule_interval='50 * * * *',
    catchup=False,
    tags=['dps-dashboard']
)
def test_dag():
    upstream = EmptyOperator(task_id="start")

    @task(task_id="test")
    def test():
        uri = "postgresql://wayu:xTUu28E5@10.121.101.144:5432/dvdrental"
        query = "SELECT * FROM actor"
        try:
            df = pl.read_database_uri(query, uri, engine="connectorx")
        except:
            df = pl.read_database_uri(query, uri, engine="adbc")

    downstream = EmptyOperator(task_id="end")

    upstream >> test() >> downstream

test_dag()



