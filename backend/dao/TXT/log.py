import datetime as datetime
import sys
sys.path.append('.')

root = 'backend/files/log.txt'

def create_log(data: str):
    try:
        with open(root, 'a') as file:
            file.write(data+'\n')
        return True
    except Exception as e:
        print(e)
        return False


def read_logs():
    list_log = []
    file_log = open(root, 'r')
    for l in file_log:
        log = l.strip().split('|')
        log[2] = log[2].strip()
        list_log.append(log)
    return list_log
