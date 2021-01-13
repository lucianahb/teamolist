from backend.dao.BD.bd_config import generate_connection
from backend.models.product import Product


def create_product(product:Product):
    conn = generate_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO product (name, description, price) VALUES ('{product.name}','{product.description}',{product.price});"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()
    

def read_products():
    products = []
    conn = generate_connection()
    cursor = conn.cursor()

    cursor.execute('select * from product')

    product_list = cursor.fetchall()

    for p in product_list:
        products.append(Product(p[1], p[2], p[3], p[0]))
    cursor.close()
    conn.close()

    return products
        