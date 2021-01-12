import datetime as datetime
import sys

import psycopg2
sys.path.append('.')

root = '../../backend/files/log.txt'
host = "pgsql08-farm15.uni5.net"
user = "topskills1"
password = "olist21"
database = "topskills1"
connection_string = f"host={host} dbname={database} user={user} password={password}"

def create_log(data: str):
    try:
        conn = psycopg2.connect(connection_string)
        
        with conn.cursor() as cur:
            cur.execute(f'''
            INSERT INTO log (name, description) VALUES ('{name}', '{description}');
            ''')

        conn.commit()
    except Exception as e:
        print("deu ruim")
        print(e)

    finally:
        pass
        conn.close()


def read_logs():
    list_log = []
    file_log = open(root, 'r')
    for l in file_log:
        log = l.strip().split('|')
        log[2] = log[2].strip()
        list_log.append(log)
    return list_log
