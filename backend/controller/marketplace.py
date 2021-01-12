from backend.dao.BD.marketplace import create_mkplace, read_mkplaces
from backend.models.marketplace import Marketplace
from backend.controller.log import write_log, list_logs


def write_mkplace(marketplace: Marketplace):
    create_mkplace(marketplace)
    operation_type = 1 #1=write and 2=list
    write_log('writen Marketplace', operation_type)

def list_mkplaces():
    marketplaces = read_mkplaces()
    operation_type = 2 #1=write and 2=list
    write_log('Listed Marketplace', operation_type)
    return marketplaces