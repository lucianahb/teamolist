root = 'backend/files/list_category.txt'

from backend.dao.category import create_category # pylint: disable=import-error 
from backend.dao.category import read_categories # pylint: disable=import-error 

def write_category(data:str)->None:
    create_category(data)


def list_categories()->list:
    return read_categories()