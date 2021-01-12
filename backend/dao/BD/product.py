from backend.dao.BD.bd_config import generate_connection_string # pylint: disable=import-error 
import psycopg2


def create_product(data: str):
    try:
        conn = psycopg2.connect(generate_connection_string())
        cursor = conn.cursor()
        query = f"insert into product (name,description,price) values('{data[0]}','{data[1]}',{data[2]})"
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    

def read_products():
    try:
        data = []
        conn = psycopg2.connect(generate_connection_string())
        cursor = conn.cursor()

        cursor.execute('select * from product')

        product = cursor.fetchall()

        for p in product:
            data.append([p[1], p[2],p[3]])

        return data

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

