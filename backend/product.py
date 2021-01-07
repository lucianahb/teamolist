def save_product(data: str):
    root = 'backend/files/'
    full_path = f'{root}list_product.txt'
    try:
        file_product = open(full_path, 'a')
        file_product.write(data+'\n') #'%\n'
        return True
    except Exception as e:
        return False
    finally:
        file_product.close()


def list_products():
    list_prod = []
    root = 'backend/files/'
    full_path = f'{root}list_product.txt'
    file_prod = open(full_path, 'r')
    for f in  file_prod:
        prod = f.strip().split(';')
        list_prod.append(prod)
    return list_prod
