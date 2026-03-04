import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

engine = create_engine(url)
tables = ['customers', 'orders', 'payments', 'support_tickets']

for table in tables:
    df = pd.read_sql_table(table, engine)
    df.to_csv(f"/opt/airflow/data/raw/{table}.csv", index=False)
    print(f"Exported {table} to CSV.")
