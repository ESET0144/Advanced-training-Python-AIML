# import required libraries
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator, get_current_context
import pandas as pd
from sqlalchemy import create_engine

# Define default arguments for the DAG
with DAG(
    dag_id="sample_elt_dag",
    #default_args= default_args,
    description = "A simple ELT pipeline example",
    start_date= datetime(2025, 11, 11),
    schedule= " */2 * * * *",
    catchup = False,
    tags = ["example", "elt", "training"],
) as dag:
    
    def extract_data():
        data = pd.read_csv("iris.csv")
        print("Extracted data:", data)
        return data
    
    def load_data():
        context = get_current_context()
        extracted_data = context["ti"].xcom_pull(task_ids = "extract_task")
        #loaded_data.to_csv("loaded_data.csv")

        # Create SQLAlchemy engine (connect to Astro Postgres)
        engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres:5432/airflow_db")

        # Write DataFrame to Postgres table
        extracted_data.to_sql(
            name="iris_data",        # table name in Postgres
            con=engine,
            if_exists="append",     # or "append"
            index=False
        )

        print("✅ Data successfully stored in Postgres table 'iris_data'")
        return extracted_data

    def transform_data():
        context = get_current_context()
        transformed_data = context["ti"].xcom_pull(task_ids = "load_task")
        transformed_data = [item.upper() for item in transformed_data]
        print(" Transformed data:", transformed_data)
        return transformed_data

    extract_task = PythonOperator(
        task_id = "extract_task",
        python_callable = extract_data,
    )

    load_task = PythonOperator(
        task_id = "load_task",
        python_callable = load_data,
    )

    transform_task = PythonOperator(
        task_id = "transform_task",
        python_callable = transform_data,
    )

    extract_task  >> load_task >> transform_task
