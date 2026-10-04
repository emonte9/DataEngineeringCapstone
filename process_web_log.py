# import the libraries
from datetime import timedelta
from airflow.utils.dates import days_ago
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
# Operators; you need this to write tasks!
# from airflow.operators.bash_operator import BashOperator
from airflow.operators.bash import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago
#defining DAG arguments
# You can override them on a per-task basis during operator initialization

default_args = {
'owner': 'Edgar',
'start_date': days_ago(0),
'email': ['your_email_here'],
'retries': 1,
'retry_delay': timedelta(days=1),
}


# defining the DAG
# define the DAG
process_web_log = DAG(
'process_web_log',
default_args=default_args,
description='process_web_log',
schedule_interval=timedelta(days=1),
)

extract_data = BashOperator(
task_id='extract_data',
bash_command='cut -d" " -f1 /home/project/airflow/dags/capstone/accesslog.txt > /home/project/airflow/dags/capstone/extracted_data.txt ',
dag=process_web_log,
)


transform_data = BashOperator(
task_id='transform_data',
bash_command='grep -vF "198.46.149.143" /home/project/airflow/dags/capstone/extracted_data.txt > /home/project/airflow/dags/capstone/transformed_data.txt ',
dag=process_web_log,
)

load_data = BashOperator(
    task_id = 'load_data',
    bash_command='tar -cvf /home/project/airflow/dags/capstone/weblog.tar /home/project/airflow/dags/capstone/transformed_data.txt ',
    dag=process_web_log,
)



extract_data >> transform_data >> load_data


