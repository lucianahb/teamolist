from backend.dao.BD.bd_config import generate_connection_string # pylint: disable=import-error 
from backend.models.seller import Seller
import psycopg2


def create_seller(seller: Seller):
    try:
        conn = psycopg2.connect(generate_connection_string())
        cursor = conn.cursor()
        query = f"insert into seller (fullname,email,phone) values('{seller.name}','{seller.phone}',{seller.email})"
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    

def read_sellers():
    try:
        data = []
        conn = psycopg2.connect(generate_connection_string())
        cursor = conn.cursor()
        cursor.execute('select * from seller')
        result = cursor.fetchall()
        lista_sellers = []
        for seller in result:
            sell = Seller(seller[1], seller[3], seller[2])
            lista_sellers.append(sell)
        return lista_sellers

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


