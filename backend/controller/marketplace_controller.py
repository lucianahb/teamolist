from backend.controller.base_controller import BaseController
from backend.dao.BD.marketplace_dao import MarketplaceDao
from backend.models.log import Log

class MarketplaceController(BaseController):
    def __init__(self):
        self.__dao = MarketplaceDao()
        log = Log('', 'Marketplace')
        super().__init__(self.__dao, log)