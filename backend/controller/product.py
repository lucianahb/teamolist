from backend.dao.BD.product import create_product, read_products
from backend.models.product import Product
from backend.controller.log import write_log, list_logs


def write_product(product: Product):
    create_product(product)
    operation_type = 1 #1=write and 2=list
    write_log('writen Product', operation_type)


def list_products():
    products = read_products()
    operation_type = 2 #1=write and 2=list
    write_log('writen Product', operation_type)
    return products
