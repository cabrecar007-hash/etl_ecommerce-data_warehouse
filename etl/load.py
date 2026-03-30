import psycopg2

def load_fact_user_activity(rows, pg_config):
    conn = psycopg2.connect(**pg_config)
    cursor = conn.cursor()
    for row in rows:
        cursor.execute("""
            INSERT INTO fact_user_activity 
            (store_id, user_id, action_type, product_id, amount, datetime)
            VALUES (%s,%s,%s,%s,%s,%s)
            ON CONFLICT DO NOTHING
        """, (row['store_id'], row['user_id'], row['action_type'], row['product_id'], row['amount'], row['datetime']))
    conn.commit()
    cursor.close()
    conn.close()

def load_dimension_table(rows, table_name, pg_config, columns):
    conn = psycopg2.connect(**pg_config)
    cursor = conn.cursor()
    for row in rows:
        values = tuple(row[col] for col in columns)
        placeholders = ','.join(['%s']*len(columns))
        cursor.execute(f"""
            INSERT INTO {table_name} ({','.join(columns)})
            VALUES ({placeholders})
            ON CONFLICT DO NOTHING
        """, values)
    conn.commit()
    cursor.close()
    conn.close()
