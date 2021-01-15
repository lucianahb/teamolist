from backend.controller.base_controller import BaseController
from backend.dao.BD.seller import SellerDao
from backend.models.log import Log


class SellerController(BaseController):
    def __init__(self):
        self.__dao = SellerDao()
        log = Log('', 'Seller')
        super().__init__(self.__dao, log)