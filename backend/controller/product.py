from backend.dao.BD.product import create_product, read_products, get_by_id, u_product, d_product
from backend.models.product import Product
from backend.controller.log import write_log, list_logs
from backend.models.log import Log
import datetime as datetime

def write_product(product: Product):
    create_product(product)
    date = datetime.datetime.now()
    log = Log(date, f'Create Product {product.name}')
    write_log(log)

def list_products():
    products = read_products()
    date = datetime.datetime.now()
    log = Log(date, 'Listed Products')
    write_log(log)
    return products

def get_product_by_id(id: int):
    product = get_by_id(id)
    date = datetime.datetime.now()
    log = Log(date, f'Read product by id: {id}')
    write_log(log)
    return product

def update_product(product: Product):
    u_product(product)
    date = datetime.datetime.now()
    log = Log(date, f'Update product {product.name}')
    write_log(log)

def delete_product(product: Product):
    d_product(product)
    date = datetime.datetime.now()
    log = Log(date, f'Delete product {product.name}')
    write_log(log)