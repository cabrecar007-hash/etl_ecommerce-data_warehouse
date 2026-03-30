import mysql.connector
import yaml

def extract_table(store, db_config, table_name):
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=store['db_name']
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
