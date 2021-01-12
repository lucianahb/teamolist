from backend.dao.BD.marketplace import create_mkplace, read_mkplaces
from backend.models.marketplace import Marketplace
from backend.controller.log import write_log, list_logs
from backend.models.log import Log
import datetime as datetime

def write_mkplace(marketplace: Marketplace):
    create_mkplace(marketplace)
    date = datetime.datetime.now()
    log = Log(date, 'writen Marketplace')
    write_log(log)

def list_mkplaces():
    marketplaces = read_mkplaces()
    date = datetime.datetime.now()
    log = Log(date, 'Listed Marketplaces')
    write_log(log)
    return marketplaces