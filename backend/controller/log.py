import datetime as datetime
import sys
from backend.models.log import Log
sys.path.append('.')
from backend.dao.BD.log import create_log, read_logs # pylint: disable=import-error 

def write_log(log: Log):
    create_log(log)
   
def list_logs():
    list_log = read_logs()
    return list_log