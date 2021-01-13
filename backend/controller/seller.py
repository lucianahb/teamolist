#from backend.dao.TXT.seller import  create_seller, read_sellers  # pylint: disable=import-error 
from backend.dao.BD.seller import create_seller, read_sellers, list_by_id, update_seller, del_seller
from backend.controller.log import write_log
from backend.models.seller import Seller
from backend.models.log import Log
import datetime as datetime

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

def list_seller_by_id(id: int) -> Seller:
    seller = list_by_id(id)
    date = datetime.datetime.now()
    log = Log(date, 'Listed Sellers by id')
    write_log(log)
    return seller

def update_sel(seller: Seller) ->None:
    update_seller(seller)
    date = datetime.datetime.now()
    log = Log(date, 'Updated Seller')
    write_log(log)

def del_sel(id: int) -> None:
    del_seller(id)
    date = datetime.datetime.now()
    log = Log(date, 'Deleted Seller')
    write_log(log)