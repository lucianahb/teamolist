root = 'backend/files/list_seller.txt'

def create_seller(data:str):
    try:
        with open(root, 'a') as file:
            formated_data = f'{data[0]};{data[1]};{data[2]}'
            file.write(formated_data+'\n')
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
