import sys
from backend.models.log import Log
import psycopg2
sys.path.append('.')
from backend.dao.BD.bd_config import generate_connection

def create_log(log: Log):
    conn = generate_connection()
    
    with conn.cursor() as cur:
        cur.execute(f'''
        INSERT INTO log (datetime, action) VALUES ('{log.datetime}', '{log.action}');
        ''')
    conn.close()


def read_logs():
    try:
        conn = psycopg2.connect(connection_string)
        
        with conn.cursor() as cur:
            cur.execute('select datetime, action, id from log')
            lista_log = []
            result = cur.fetchall()
            for log in result:
                l = Log(log[0],log[1],log[2])
                lista_log.append(l)
            return lista_log
    except Exception as e:
        print(e)

    finally:
        conn.close()
