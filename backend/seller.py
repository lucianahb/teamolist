root = 'backend/files/list_seller.txt'

def save_seller(data:str):
    try:
        file_seller = open(root, 'a')
        file_seller.write(data+'\n') 
        return True
    except Exception as e:
        return False
    finally:
        file_seller.close()


def list_sellers():
    list_seller = []
    file_seller = open(root, 'r')
    for f in  file_seller:
        seller = f.strip().split(';')
        list_seller.append(seller)
    return list_seller
