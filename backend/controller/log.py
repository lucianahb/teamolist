import datetime as datetime
import sys
sys.path.append('.')
from backend.dao.BD.log import create_log, read_logs # pylint: disable=import-error 

def write_log(function_name: str, operation_type: str):
    create_log(function_name, operation_type)
   
def list_logs():
    return read_logs()