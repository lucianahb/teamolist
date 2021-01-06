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


def list_all():
    pass

