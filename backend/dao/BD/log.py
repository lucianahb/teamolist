import sys
from backend.models.log import Log
from backend.dao.BD.bd_config import connection_credentials
import psycopg2

sys.path.append('.')


def create_log(log: Log):
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()
            cur.execute(f'''
            INSERT INTO log (datetime, action) VALUES ('{log.datetime}', '{log.action}');
            ''')
    except Exception as e:
        print(e)


def read_logs():
    lista_log = []
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()
            cur.execute('select datetime, action, id from log')
            result = cur.fetchall()
            for log in result:
                l = Log(log[0],log[1],log[2])
                lista_log.append(l)
    except Exception as e:
        print(e)
    return logs
