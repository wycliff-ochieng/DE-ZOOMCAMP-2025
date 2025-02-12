
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import argparse

def main(params):
    df = pd.read_csv(r"\Users\Admin\Desktop\2025-ZOOM\Docker-IaC\yellow_tripdata_2024-01.csv")
    df.head(10)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime )
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    print(pd.io.sql.get_schema(df,name="yellow_taxi"))

    conn = psycopg2.connect(
        host='localhost',
        port=5433,
        user='postgres',
        database='postgres',
        password='mGFeanZG'
    )

    cursor = conn.cursor()

    engine = create_engine('postgresql+psycopg2://', creator=lambda:conn)

    create_query_file = open("../data/create_table.sql")
    create_query = create_query_file.read()
    create_query

    cursor.execute(create_query)

    df_iter = pd.read_csv(r"\Users\Admin\Desktop\2025-ZOOM\Docker-IaC\yellow_tripdata_2024-01.csv",iterator=True,chunksize=1000)
    chunk = next(df_iter)
    merge_query_file = open("../data/insert.sql")
    merge_query = merge_query_file.read()
    merge_query


     
    for chunk in df_iter:
        cursor.executemany(merge_query,chunk.to_dict(orient="records"))

    df.head(n=0)

if "__name__" == "__main___":
    params.

