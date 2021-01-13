from backend.dao.BD.marketplace import create_mkplace, read_mkplaces, list_by_id, update_marketplace, del_marketplace
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

def list_mkplace_by_id(id: int) -> Marketplace:
    marketplace = list_by_id(id)
    date = datetime.datetime.now()
    log = Log(date, 'Listed Marketplaces by id')
    write_log(log)
    return marketplace

def update_mkplace(marketplace: Marketplace):
    update_marketplace(marketplace)
    date = datetime.datetime.now()
    log = Log(date, 'Updated Marketplace')
    write_log(log)

def del_mkplace(id: int) -> None:
    del_marketplace(id)
    date = datetime.datetime.now()
    log = Log(date, 'Deleted Marketplace')
    write_log(log)
