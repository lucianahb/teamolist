from backend.dao.BD.bd_config import connection_credentials
from backend.models.product import Product
import psycopg2


def create_product(product:Product):
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            query = f"INSERT INTO product (name, description, price) VALUES ('{product.name}','{product.description}',{product.price});"
            cursor.execute(query)
            conn.commit()
    except Exception as e:
        print(e)

def read_products():
    products = []
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute('select * from product')
            product_list = cursor.fetchall()
            for p in product_list:
                products.append(Product(p[1], p[2], p[3], p[0]))
    except Exception as e:
        print(e)
    return products
        