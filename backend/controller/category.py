from backend.dao.BD.category import create_category, read_categories # pylint: disable=import-error 
from backend.controller.log import write_log
from backend.models.category import Category
from backend.models.log import Log
import datetime as datetime
#from backend.dao.TXT.category import create_category, read_categories # pylint: disable=import-error 

def write_category(category: Category)->None:
    create_category(category)
    date = datetime.datetime.now()
    log = Log(date, 'writen Category')
    write_log(log)


def list_categories()->list:
    categories = read_categories()
    date = datetime.datetime.now()
    log = Log(date, 'Listed Category')
    write_log(log)
    return categories