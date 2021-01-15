from backend.models.log import Log
from backend.controller.log import LogController
import datetime as datetime


class BaseController:
    def __init__(self, dao, log: Log):
        self.__dao = dao
        self.__log = log

    def create(self, model: object)->None:
        self.__dao.create(model)
        self.__log.action = f'Create {self.__log.action} {model.name}'
        self.__log.datetime = datetime.datetime.now()
        LogController().create(self.__log)
        
    def read_by_id(self,id:int)-> object:
        objetc_by_id = self.__dao.read_by_id(id)
        self.__log.action = f'Read {self.__log.action} by id: {id}'
        self.__log.datetime = datetime.datetime.now()
        LogController().create(self.__log)
        return objetc_by_id

    def read_all(self)->list:
        list_all = self.__dao.read_all()
        self.__log.action = f'Read all {self.__log.action}'
        self.__log.datetime = datetime.datetime.now()
        LogController().create(self.__log)
        return list_all

    def delete(self, id:int)->None:
        self.__dao.delete(id)
        self.__log.action = f'Delete {self.__log.action}: {id}'
        self.__log.datetime = datetime.datetime.now()
        LogController().create(self.__log)

    def update(self, model: object)->None:
        self.__dao.update(model)
        self.__log.action = f'Update {self.__log.action}: {model.id}'
        self.__log.datetime = datetime.datetime.now()
        LogController().create(self.__log)

