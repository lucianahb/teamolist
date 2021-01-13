#from backend.dao.TXT.seller import  create_seller, read_sellers  # pylint: disable=import-error 
from backend.dao.BD.seller import create_seller, read_sellers
from backend.controller.log import write_log
from backend.models.seller import Seller

def write_seller(seller:Seller) -> None:
    create_seller(seller)
    date = datetime.datetime.now()
    log = Log(date, 'writen Seller')
    write_log(log)

def list_sellers() -> list:
    sellers = read_sellers()
    date = datetime.datetime.now()
    log = Log(date, 'Listed Sellers')
    write_log(log)
    return sellers
