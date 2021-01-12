root = '../backend/files/list_category.txt'
from backend.dao.BD.category import create_category, read_categories # pylint: disable=import-error 
from backend.controller.log import write_log
from backend.models.category import Category
#from backend.dao.TXT.category import create_category, read_categories # pylint: disable=import-error 

def write_category(category: Category)->None:
    create_category(category)
    write_log('writen Category', 1) #1=write and 2=list
    print("Category written")


def list_categories()->list:
    operation_type = 2 #1=write and 2=list
    write_log('Listed Category', operation_type)
    return read_categories()