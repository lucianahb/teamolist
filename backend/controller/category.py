from backend.controller.base_controller import BaseController
from backend.dao.BD.category import CategoryDao


class CategoryController(BaseController):
    def __init__(self):
        self.__dao = CategoryDao()
        super().__init__(self.__dao)