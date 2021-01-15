from backend.controller.base_controller import BaseController
from backend.dao.BD.seller import SellerDao
from backend.models.log import Log


class SellerController(BaseController):
    def __init__(self, log: Log):
        self.__dao = SellerDao()
        super().__init__(self.__dao, log)