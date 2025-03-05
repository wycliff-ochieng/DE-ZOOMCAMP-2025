FROM python:3.12

RUN pip install pandas psycopg2 schlachemy

WORKDIR /app

COPY ingestion.py ingestion.py

ENTRYPOINT ["python","ingestion.py"]