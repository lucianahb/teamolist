from backend.dao.BD.category import create_category, read_categories, get_by_id, u_category, d_category # pylint: disable=import-error 
from backend.controller.log import write_log
from backend.models.category import Category
from backend.models.log import Log
import datetime as datetime
#from backend.dao.TXT.category import create_category, read_categories # pylint: disable=import-error 

def write_category(category: Category)->None:
    create_category(category)
    date = datetime.datetime.now()
    log = Log(date, f'Create Category {category.name}')
    write_log(log)


def list_categories()->list:
    categories = read_categories()
    date = datetime.datetime.now()
    log = Log(date, 'Read Categories')
    write_log(log)
    return categories


def get_category_by_id(id: int):
    category = get_by_id(id)
    date = datetime.datetime.now()
    log = Log(date, f'Read Category by id: {id}')
    write_log(log)
    return category

def update_category(category: Category):
    u_category(category)
    date = datetime.datetime.now()
    log = Log(date, f'Update Category {category.name}')
    write_log(log)

def delete_category(category: Category):
    d_category(category)
    date = datetime.datetime.now()
    log = Log(date, f'Delete Category {category.name}')
    write_log(log)
