from backend.models.category import Category
from backend.dao.BD.bd_config import generate_connection
root = '../../backend/files/list_category.txt'


def create_category(category: Category)->None:
    conn = generate_connection()
    cur = conn.cursor()
    cur.execute(f'''
    INSERT INTO category (name, description) VALUES ('{category.name}','{category.description}');
    ''')

    conn.commit()
    cur.close()
    conn.close()


def read_categories()->list:
    conn = generate_connection()
    cur = conn.cursor()
    cur.execute('select * from category')
    list_categories = []
    result = cur.fetchall()
    for category in result:
        cat = Category(category[1],category[2],category[0])
        list_categories.append(cat)
    
    cur.close()
    conn.close()

    return list_categories
