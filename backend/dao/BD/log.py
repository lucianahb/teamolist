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

def create_log(function_name: str, operation_type: str):
    date = datetime.datetime.now()
    
    try:
        conn = psycopg2.connect(connection_string)
        
        with conn.cursor() as cur:
            cur.execute(f'''
            INSERT INTO log (datetime, action) VALUES ('{date}', '{function_name}');
            ''')

        conn.commit()
    except Exception as e:
        print("deu ruim")
        print(e)

    finally:
        pass
        conn.close()


def read_logs():
    try:
        conn = psycopg2.connect(connection_string)
        
        with conn.cursor() as cur:
            cur.execute('select * from log')
            
            result = cur.fetchall()
            print(result)
            return result
    except Exception as e:
        print(e)

    finally:
        conn.close()
