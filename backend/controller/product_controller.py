from backend.controller.base_controller import BaseController
from backend.dao.BD.product_dao import ProductDao
from backend.models.log import Log

class ProductController(BaseController):
    def __init__(self):
        self.__dao = ProductDao()
        log = Log('', 'Product')
        super().__init__(self.__dao, log)