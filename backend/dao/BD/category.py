root = '../../backend/files/list_category.txt'


import psycopg2
host = "pgsql08-farm15.uni5.net"
user = "topskills1"
password = "olist21"
database = "topskills1"
connection_string = f"host={host} dbname={database} user={user} password={password}"

def create_category(name:str)->None:
    try:
        conn = psycopg2.connect(connection_string)
        
        with conn.cursor() as cur:
            cur.execute(f'''
            INSERT INTO category (name) VALUES ('{name}');
            ''')

        conn.commit()
    except Exception as e:
        print("deu ruim")
        print(e)

    finally:
        pass
        conn.close()


def read_categories()->list:
    try:
        conn = psycopg2.connect(connection_string)
        
        with conn.cursor() as cur:
            cur.execute('select * from category')
            
            result = cur.fetchall()
            return result
    except Exception as e:
        print(e)

    finally:
        conn.close()
