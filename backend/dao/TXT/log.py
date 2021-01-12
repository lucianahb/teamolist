import datetime as datetime
import sys
sys.path.append('.')

root = 'backend/files/log.txt'

def create_log(function_name: str, operation_type: str):
    date = datetime.datetime.now()
    date = date.strftime("%d/%m/%Y | %H:%M:%S")
    data = f"{date} | {operation_type} | {function_name}\n"
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
