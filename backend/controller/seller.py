#from backend.dao.TXT.seller import  create_seller, read_sellers  # pylint: disable=import-error 
from backend.dao.BD.seller import create_seller, read_sellers
from backend.controller.log import write_log
from backend.models.seller import Seller

def write_seller(seller:Seller) -> None:
    create_seller(seller)
    operation_type = 1 #1=write and 2=list
    write_log('writen Seller', operation_type)

def list_sellers() -> list:
    sellers = read_sellers()
    operation_type = 2 #1=write and 2=list
    write_log('Listed Seller', operation_type)
    return sellers
