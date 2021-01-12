import os
print(os.listdir())
root = 'backend/files/list_seller.txt'

def create_seller(data:str):
    try:
        with open(root, 'a') as file:
            file.write(data+'\n')
        return True
    except Exception as e:
        print(e)
        return False


def read_sellers():
    list_seller = []
    file_seller = open(root, 'r')
    for f in  file_seller:
        seller = f.strip().split(';')
        list_seller.append(seller)
    return list_seller
