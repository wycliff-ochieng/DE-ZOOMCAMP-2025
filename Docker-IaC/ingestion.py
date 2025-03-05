

import pandas as pd
from sqlalchemy import create_engine
import psycopg2

df = pd.read_csv(r"\Users\Admin\Desktop\2025-ZOOM\Docker-IaC\yellow_tripdata_2024-01.csv")
def main(df):
    df.head(10)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime )
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    #engine = create_engine('postgresql://postgres:mGFeanZG@localhost:5433/postgres')

    return df

def create_ingest_tables():
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

    print(chunk.dtypes)

    for chunk in df_iter:
        data = [tuple(row) for row in chunk.to_numpy()]
        cursor.executemany(merge_query,data)


    info = """SELECT * FROM "yellow_taxi" LIMIT 50 """
    info2 = pd.read_sql(info,conn)
    print(info2)

    conn.rollback()

if __name__ == "__main__":
    create_ingest_tables()

