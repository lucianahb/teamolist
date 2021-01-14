from backend.dao.BD.bd_config import Connection
from backend.models.seller import Seller
import psycopg2

def create_seller(seller: Seller) -> None:
    try:
        with Connection() as conn:
            cursor = conn.cursor()
            query = f"insert into seller (name, phone, mail) values('{seller.name}','{seller.phone}','{seller.email}')"
            cursor.execute(query)
            conn.commit()
    except Exception as e:
        print(e)

def read_sellers() -> list:
    lista_sellers = []
    try:
       with Connection() as conn:
            cursor = conn.cursor()
            cursor.execute('select * from seller')
            result = cursor.fetchall()
            for seller in result:
                sell = Seller(seller[1], seller[2], seller[3],seller[0])
                lista_sellers.append(sell)
    except Exception as e:
        print(e)
    return lista_sellers

def list_by_id(id: int) -> Seller:
    sel = []
    try:
       with Connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM seller where id = {id}')
            seller = cursor.fetchone()
            sel = Seller(seller[1],seller[2],seller[3],seller[0])
    except Exception as e:
        print(e)
    return sel

def update_seller(seller: Seller) -> None:
    try:
        with Connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE seller set name = '{seller.name}', phone='{seller.phone}', mail='{seller.email}' where id = '{seller.id}'")
            conn.commit()
    except Exception as e:
        print(e)

def del_seller(id: int) ->None:
    try:
        with Connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM seller where id = '{id}'")
            conn.commit()
    except Exception as e:
        print(e)
    
