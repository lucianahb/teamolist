from backend.dao.BD.bd_config import connection_credentials
from backend.models.seller import Seller
import psycopg2

def create_seller(seller: Seller):
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            query = f"insert into seller (name, phone, mail) values('{seller.name}','{seller.phone}','{seller.email}')"
            cursor.execute(query)
            conn.commit()
    except Exception as e:
        print(e)

def read_sellers():
    lista_sellers = []
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute('select * from seller')
            result = cursor.fetchall()
            for seller in result:
                sell = Seller(seller[1], seller[2], seller[3],seller[0])
                lista_sellers.append(sell)
    except Exception as e:
        print(e)
    return lista_sellers


