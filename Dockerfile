FROM apache/airflow:2.9.2

# TODO: consider install requirements here
RUN python -m pip install --upgrade pip
COPY requirements.txt /
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt

