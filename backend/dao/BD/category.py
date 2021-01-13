from backend.models.category import Category
from backend.dao.BD.bd_config import connection_credentials
import psycopg2


def create_category(category: Category)->None:
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()
            cur.execute(f'''
            INSERT INTO category (name, description) VALUES ('{category.name}','{category.description}');''')
            conn.commit()
    except Exception as e:
        print(e)

def read_categories()->list:
    list_categories = []
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()
            cur.execute('select * from category')
            result = cur.fetchall()
            
            for category in result:
                cat = Category(category[1],category[2],category[0])
                list_categories.append(cat)
    except Exception as e:
        print(e)
    return list_categories
