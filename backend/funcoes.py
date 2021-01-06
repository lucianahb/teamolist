import datetime as datetime
import sys
from .marketplace import save_mkp
from .product import save_product
sys.path.append('.')


def write_file(type_file: int, data: str) -> bool:
    if type_file == 0:
        save_mkp(data)
        log('save_mkp')
    elif type_file == 1:
        save_product(data)
        log('save_product')


def log(function_name: str):
    root = 'backend/files/'
    files = open(f'{root}log.txt', 'a')
    data = datetime.datetime.now()
    files.write(data.strftime(
        f"%d/%m/%Y às %H:%M:%S => Acesso a função {function_name}\n"))
    files.close()
