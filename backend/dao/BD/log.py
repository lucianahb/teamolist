import sys
from backend.models.log import Log
from backend.dao.BD.bd_config import Connection
import psycopg2

sys.path.append('.')


def create_log(log: Log):
    try:
        with Connection() as conn:
            cur = conn.cursor()
            cur.execute(f'''
            INSERT INTO log (datetime, action) VALUES ('{log.datetime}', '{log.action}');
            ''')
    except Exception as e:
        print(e)


def read_logs():
    lista_log = []
    try:
        with Connection() as conn:
            cur = conn.cursor()
            cur.execute('select datetime, action, id from log')
            result = cur.fetchall()
            for log in result:
                l = Log(log[0],log[1],log[2])
                lista_log.append(l)
    except Exception as e:
        print(e)
    return lista_log



# class LogDao(BaseDao):
#     def create(self, model: Log) -> None:
#         query = f"INSERT INTO log (datetime, action) VALUES ('{model.datetime}', '{model.action}');"
#         super().execute(query)

#     def read_all(self)->list:
#         query = 'SELECT datetime, action, id FROM log;'
#         result_list = super().read(query)
#         logs = []
#         for result in result_list:
#             logs.append(Log(result[0], result[1], result[2], result[3]))
#         return logs