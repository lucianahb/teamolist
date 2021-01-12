from backend.models.category import Category
root = '../../backend/files/list_category.txt'


import psycopg2
host = "pgsql08-farm15.uni5.net"
user = "topskills1"
password = "olist21"
database = "topskills1"
connection_string = f"host={host} dbname={database} user={user} password={password}"

def create_category(category: Category)->None:
    try:
        conn = psycopg2.connect(connection_string)
        print(category.name)
        with conn.cursor() as cur:
            cur.execute(f'''
            INSERT INTO category (name, description) VALUES ('{category.name}','{category.description}');
            ''')

        conn.commit()
    except Exception as e:
        print(e)

    finally:
        pass
        conn.close()


def read_categories()->list:
    try:
        conn = psycopg2.connect(connection_string)
        
        with conn.cursor() as cur:
            
            cur.execute('select * from category')
            list_categories = []
            result = cur.fetchall()
            for category in result:
                cat = Category(category[1],category[2])
                list_categories.append(cat)
            return list_categories
    except Exception as e:
        print(e)

    finally:
        conn.close()
