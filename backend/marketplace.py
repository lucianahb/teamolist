def save_mkplace(data:str):
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


def list_mkplaces():
    list_mkp = []
    root = 'backend/files/'
    full_path = f'{root}list_marketplace.txt'
    file_mkp = open(full_path, 'r')
    for f in  file_mkp:
        mkp = f.strip().split(';')
        list_mkp.append(mkp)
    return list_mkp
