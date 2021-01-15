from backend.models.log import Log
from backend.controller.log import write_log

class BaseController:
    def __init__(self, dao, log: Log):
        self.__dao = dao
        self.__log = log
    def create(self, model: object)->None:
        self.__dao.create(model)
        write_log(self.__log)

    def read_by_id(self,id:int)-> object:
        objetc_by_id = self.__dao.read_by_id(id)
        write_log(self.__log)
        return objetc_by_id

    def read_all(self)->list:
        list_all = self.__dao.read_all()
        write_log(self.__log)
        return list_all

    def delete(self, id:int)->None:
        self.__dao.delete(id)
        write_log(self.__log)

    def update(self, model: object)->None:
        self.__dao.update(model)
        write_log(self.__log)

