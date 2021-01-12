root = 'backend/files/list_marketplace.txt'

def create_mkplace(data:str):
    try:
        with open(root, 'a') as file:
            file.write(data+'\n')
        return True
    except Exception as e:
        print(e)
        return False


def read_mkplaces():
    list_mkp = []
    file_mkp = open(root, 'r')
    for f in  file_mkp:
        mkp = f.strip().split(';')
        list_mkp.append(mkp)
    return list_mkp
