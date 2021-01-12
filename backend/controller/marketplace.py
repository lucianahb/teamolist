from backend.dao.BD.marketplace import create_mkplace, read_mkplaces
from backend.models.marketplace import Marketplace

def write_mkplace(marketplace: Marketplace):
    create_mkplace(marketplace)

def list_mkplaces():
    return read_mkplaces()