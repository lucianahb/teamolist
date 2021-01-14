from backend.models.category import Category
from backend.dao.BD.bd_config import Connection
import psycopg2


def create_category(category: Category) -> None:
    try:
        with Connection() as conn:
            cur = conn.cursor()
            cur.execute(f'''
            INSERT INTO category (name, description) VALUES ('{category.name}','{category.description}');''')
            conn.commit()
    except Exception as e:
        print(e)

def read_categories() -> list:
    list_categories = []
    try:
        with Connection() as conn:
            cur = conn.cursor()
            cur.execute('select * from category')
            result = cur.fetchall()
            
            for category in result:
                cat = Category(category[1],category[2],category[0])
                list_categories.append(cat)
    except Exception as e:
        print(e)
    return list_categories

def get_by_id(id:int) -> Category:
    category = []
    try:
        with Connection() as conn:
            cur = conn.cursor()
            cur.execute(f'select * from category where id = {id}')
            result = cur.fetchone()
            category = Category(result[1],result[2],result[0])
            
    except Exception as e:
        print(e)
    return category

def u_category(category: Category) -> None:
    try:
        with Connection() as conn:
            cur = conn.cursor()
            cur.execute(f'''UPDATE category SET name = '{category.name}', description = '{category.description}' WHERE ID = {category.id};''')
            conn.commit()
    except Exception as e:
        print(e)

def d_category(category: Category) -> None:
    try:
        with Connection() as conn:
            cur = conn.cursor()
            cur.execute(f'''
            DELETE FROM category WHERE ID = {category.id};''')
            conn.commit()
    except Exception as e:
        print(e)

