from backend.models.log import Log
from backend.dao.BD.log import LogDao

def write_log(log: Log):
    l = LogDao()
    l.create(log)
   
def list_logs():
    l = LogDao()
    list_log = l.read_all()
    print(list_log)
    return list_log