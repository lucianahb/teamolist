from backend.dao.BD.marketplace import create_mkplace, read_mkplaces # pylint: disable=import-error 
#from backend.dao.TXT.marketplace import create_mkplace, read_mkplaces # pylint: disable=import-error 

root = '../backend/files/list_marketplace.txt'

def write_mkplace(name:str, description:str):
    create_mkplace(name, description)

def list_mkplaces():
    return read_mkplaces()