from backend.controller.base_controller import BaseController
from backend.dao.BD.category import CategoryDao
from backend.models.log import Log


class CategoryController(BaseController):
    def __init__(self, log: Log):
        self.__dao = CategoryDao()
        super().__init__(self.__dao,log)    