def save_mkp(data:str):
    root = 'backend/files/'
    full_path = f'{root}list_marketplace.txt'
    try:
        file_mkp = open(full_path, 'a')
        file_mkp.write(data+'\n') #'%\n'
        return True
    except Exception as e:
        return False
    finally:
        file_mkp.close()


def list_all():
    pass
    #root = 'backend/files/'


