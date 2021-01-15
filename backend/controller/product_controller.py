from backend.controller.base_controller import BaseController
from backend.dao.BD.product_dao import ProductDao


class ProductController(BaseController):
    def __init__(self):
        self.__dao = ProductDao()
        super().__init__(self.__dao)