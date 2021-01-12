from backend.dao.BD.product import create_product, read_products
from backend.models.product import Product
from backend.controller.log import write_log, list_logs
from backend.models.log import Log
import datetime as datetime

def write_product(product: Product):
    create_product(product)
    date = datetime.datetime.now()
    log = Log(date, 'writen Product')
    write_log(log)


def list_products():
    products = read_products()
    date = datetime.datetime.now()
    log = Log(date, 'Listed Products')
    write_log(log)
    return products
