from backend.dao.TXT.marketplace import create_mkplace, read_mkplaces # pylint: disable=import-error 

root = 'backend/files/list_marketplace.txt'

def write_mkplace(data:str):
    create_mkplace(data)

def list_mkplaces():
    return read_mkplaces()