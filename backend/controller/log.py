import datetime as datetime
import sys
sys.path.append('.')

root = '../backend/files/log.txt'

def write_log(function_name: str, operation_type: str):
    date = datetime.datetime.now()
    date = date.strftime("%d/%m/%Y | %H:%M:%S")
    data = f"{date} | {operation_type} | {function_name}\n"
    try:
        with open(root, 'a') as file:
            file.write(data)
        return True
    except Exception as e:
        print(e)
        return False
    
    

def list_logs():
    return list_logs()