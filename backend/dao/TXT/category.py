root = 'backend/files/list_category.txt'

def create_category(data:str):
    try:
        file_category = open(root, 'a')
        file_category.write(data+'\n') 
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        file_category.close()


def read_categories():
    list_category = []
    file_category = open(root, 'r')
    for f in  file_category:
        category = f.strip().split(';')
        list_category.append(category)
    return list_category
