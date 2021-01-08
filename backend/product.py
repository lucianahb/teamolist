root = 'backend/files/list_product.txt'

def save_product(data: str):
    try:
        file_product = open(root, 'a')
        file_product.write(data+'\n')
        return True
    except Exception as e:
        return False
    finally:
        file_product.close()


def list_products():
    list_prod = []
    file_prod = open(root, 'r')
    for f in  file_prod:
        prod = f.strip().split(';')
        list_prod.append(prod)
    return list_prod
