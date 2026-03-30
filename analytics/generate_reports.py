import psycopg2
import pandas as pd
from config import db_config

def run_query(query):
    conn = psycopg2.connect(**db_config['postgresql'])
    df = pd.read_sql(query, conn)
    conn.close()
    return df

query = open('analytics/queries.sql').read()
report = run_query(query)
report.to_csv('analytics/report.csv', index=False)
