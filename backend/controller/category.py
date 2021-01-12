root = '../backend/files/list_category.txt'

from backend.dao.BD.category import create_category, read_categories # pylint: disable=import-error 

#from backend.dao.TXT.category import create_category, read_categories # pylint: disable=import-error 

def write_category(name:str)->None:
    create_category(name)
    print("Category written")


def list_categories()->list:
    return read_categories()