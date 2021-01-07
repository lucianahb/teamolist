root = 'backend/files/list_marketplace.txt'

def save_mkplace(data:str):
    try:
        file_mkp = open(root, 'a')
        file_mkp.write(data+'\n') #'%\n'
        return True
    except Exception as e:
        return False
    finally:
        file_mkp.close()


def list_mkplaces():
    list_mkp = []
    file_mkp = open(root, 'r')
    for f in  file_mkp:
        mkp = f.strip().split(';')
        list_mkp.append(mkp)
    return list_mkp
