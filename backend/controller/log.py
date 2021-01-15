from backend.models.log import Log
from backend.dao.BD.log import LogDao

class LogController:
    def create(self,log: Log):
        l = LogDao()
        l.create(log)
    
    def read_all(self):
        l = LogDao()
        list_log = l.read_all()
        print(list_log)
        return list_log