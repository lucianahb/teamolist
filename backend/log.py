import datetime as datetime
import sys
sys.path.append('.')

root = 'backend/files/log.txt'

def save_log(function_name: str):
    files = open(root, 'a')
    data = datetime.datetime.now()
    files.write(data.strftime(
        f"%d/%m/%Y às %H:%M:%S | {function_name}\n"))
    files.close()
