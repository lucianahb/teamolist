
#from backend.dao.TXT.product import create_product, read_products  # pylint: disable=import-error 
from backend.dao.BD.product import create_product, read_products


root = '../backend/files/list_product.txt'

def write_product(data: str):
    create_product(data)


def list_products():
    return read_products()
