import datetime as datetime
import sys
sys.path.append('.')

root = 'backend/files/log.txt'

def save_log(function_name: str):
    files = open(root, 'a')
    data = datetime.datetime.now()
    files.write(data.strftime(
        f"%d/%m/%Y | %H:%M:%S | {function_name}\n"))
    files.close()


def list_logs():
    list_log = []
    file_log = open(root, 'r')
    for l in file_log:
        log = l.strip().split('|')
        list_log.append(log)
    return list_log
