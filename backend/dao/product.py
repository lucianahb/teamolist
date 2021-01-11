import io

root = '../backend/files/list_product.txt'

def create_product(data: str):
    try:
        with open(root, 'a') as file:
            file.write(data+'\n')
        return True
    except Exception as e:
        print(e)
        return False
    

def read_products():
    list_prod = []
    file_prod = open(root, 'r')
    for f in  file_prod:
        prod = f.strip().split(';')
        list_prod.append(prod)
    return list_prod
