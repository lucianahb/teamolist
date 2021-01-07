import datetime as datetime
import sys
sys.path.append('.')


def save_log(function_name: str):
    root = 'backend/files/'
    files = open(f'{root}log.txt', 'a')
    data = datetime.datetime.now()
    files.write(data.strftime(
        f"%d/%m/%Y às %H:%M:%S => Acesso a função {function_name}\n"))
    files.close()
