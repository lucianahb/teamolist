from backend.dao.BD.bd_config import connection_credentials
from backend.models.product import Product
import psycopg2


def create_product(product:Product) -> None:
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            query = f"INSERT INTO product (name, description, price) VALUES ('{product.name}','{product.description}',{product.price});"
            cursor.execute(query)
            conn.commit()
    except Exception as e:
        print(e)

def read_products() -> list:
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
        
    

def get_by_id(id:int) -> Product:
    product = []
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()
            cur.execute(f'select * from product where id = {id}')
            result = cur.fetchone()
            product = Product(result[1],result[2],result[3],result[0])
            
    except Exception as e:
        print(e)
    return product

def u_product(product: Product) -> None:
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()
            cur.execute(f'''UPDATE product SET name = '{product.name}', description = '{product.description}', price = '{product.price}' WHERE ID = {product.id};''')
            conn.commit()
    except Exception as e:
        print(e)

def d_product(product: Product) -> None:
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cur = conn.cursor()
            cur.execute(f'''
            DELETE FROM product WHERE ID = {product.id};''')
            conn.commit()
    except Exception as e:
        print(e)
