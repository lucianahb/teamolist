from backend.dao.BD.product import create_product, read_products
from backend.models.product import Product

root = '../backend/files/list_product.txt'

def write_product(product: Product):
    create_product(product)


def list_products():
    return read_products()
