from backend.dao.BD.base_dao import BaseDao
from backend.models.log import Log

class LogDao(BaseDao):
    def create(self, model: Log) -> None:
        query = f"INSERT INTO log (datetime, action) VALUES ('{model.datetime}', '{model.action}');"
        super().execute(query)

    def read_all(self)->list:
        query = 'SELECT datetime, action, id FROM log order by id desc;'
        result_list = super().read(query)
        logs = []
        for result in result_list:
            logs.append(Log(result[0], result[1], result[2]))
        return logs