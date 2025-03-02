#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sqlalchemy import create_engine
import psycopg2


# In[3]:


df = pd.read_csv(r"\Users\Admin\Desktop\2025-ZOOM\Docker-IaC\yellow_tripdata_2024-01.csv")
df.head(10)


# In[4]:


df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime )
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


# In[12]:


engine = create_engine('postgresql://postgres:mGFeanZG@localhost:5433/postgres')


# In[16]:


conn = engine.connect()


# In[19]:


query = """SELECT * FROM pg_catalog.pg_tables WHERE 
schemaname != 'pg_catalog' ANG schemaname != 'information_schema'; """

with engine.connect() as conn:
    pd.read_sql(query,conn)


# In[20]:


print(pd.io.sql.get_schema(df,name="yellow_taxi"))


# In[21]:


conn = psycopg2.connect(
    host='localhost',
    port=5433,
    user='postgres',
    database='postgres',
    password='mGFeanZG'
)

cursor = conn.cursor()


# In[46]:


engine = create_engine('postgresql+psycopg2://', creator=lambda:conn)


# In[47]:


create_query_file = open("../data/create_table.sql")
create_query = create_query_file.read()
create_query


# In[50]:


cursor.execute(create_query)


# In[51]:


df_iter = pd.read_csv(r"\Users\Admin\Desktop\2025-ZOOM\Docker-IaC\yellow_tripdata_2024-01.csv",iterator=True,chunksize=1000)
chunk = next(df_iter)
merge_query_file = open("../data/insert.sql")
merge_query = merge_query_file.read()
merge_query


# In[44]:


print(chunk.dtypes)


# In[52]:


for chunk in df_iter:
    data = [tuple(row) for row in chunk.to_numpy()]
    cursor.executemany(merge_query,data)


# In[ ]:


info = """SELECT * FROM "yellow_taxi" LIMIT 50 """
info2 = pd.read_sql(info,conn)
info2


# In[49]:


conn.rollback()


# In[ ]:


df.head(n=20)

