from backend.dao.seller import  create_seller, read_sellers  # pylint: disable=import-error 

root = '../backend/files/list_seller.txt'

def write_seller(data:str):
    create_seller(data)

def list_sellers():
    return read_sellers()
