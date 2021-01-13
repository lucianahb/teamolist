import datetime as datetime
import sys
from backend.dao.BD.bd_config import connection_credentials
import psycopg2


def create_log(function_name: str, operation_type: str):
    date = datetime.datetime.now()
    
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()
            cur.execute(f'''
            INSERT INTO log (datetime, action) VALUES ('{date}', '{function_name}');
            ''')
            conn.commit()
    except Exception as e:
        print(e)


def read_logs():
    logs = []
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()
            cur.execute('select * from log')
            logs = cur.fetchall()
    except Exception as e:
        print(e)
    return logs
