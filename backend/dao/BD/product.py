from backend.dao.BD.bd_config import generate_connection_string
from backend.models.product import Product
import psycopg2


def create_product(product:Product):
    try:
        conn = psycopg2.connect(generate_connection_string())
        cursor = conn.cursor()
        query = f"INSERT INTO product (name, description, price) VALUES ('{product.name}','{product.description}',{product.price});"
        cursor.execute(query)
        conn.commit()

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    

def read_products():
    try:
        products = []
        conn = psycopg2.connect(generate_connection_string())
        cursor = conn.cursor()

        cursor.execute('select * from product')

        product_list = cursor.fetchall()

        for p in product_list:
            products.append(Product(p[1], p[2], p[3], p[0]))

        return products

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
