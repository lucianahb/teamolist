import datetime as datetime
import sys
from backend.dao.BD.bd_config import generate_connection

import psycopg2
sys.path.append('.')

def create_log(function_name: str, operation_type: str):
    date = datetime.datetime.now()
    
    try:
        conn = generate_connection()
        
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
        conn = generate_connection()
        
        with conn.cursor() as cur:
            cur.execute('select * from log')
            
            result = cur.fetchall()
            print(result)
            return result
    except Exception as e:
        print(e)

    finally:
        conn.close()
