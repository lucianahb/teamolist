from backend.dao.BD.bd_config import generate_connection
from backend.models.seller import Seller


def create_seller(seller: Seller):
    conn = generate_connection()
    cursor = conn.cursor()
    query = f"insert into seller (fullname,email,phone) values('{seller.name}','{seller.phone}','{seller.email}')"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()


def read_sellers():
    conn = generate_connection()
    cursor = conn.cursor()
    cursor.execute('select * from seller')
    result = cursor.fetchall()
    lista_sellers = []
    for seller in result:
        sell = Seller(seller[1], seller[3], seller[2],seller[0])
        lista_sellers.append(sell)
    
    cursor.close()
    conn.close()
    return lista_sellers


