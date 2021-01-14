from backend.dao.BD.bd_config import Connection
from backend.models.marketplace import Marketplace
import psycopg2


def create_mkplace(marketplace: Marketplace) -> None:
    try:
        with Connection() as conn:
            cursor = conn.cursor()
            query = f"INSERT INTO marketplace (name, description) VALUES ('{marketplace.name}', '{marketplace.description}');"
            cursor.execute(query)
            conn.commit()
    except Exception as e:
        print(e)


def read_mkplaces()->list:
    marketplaces = []
    try:
        with Connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM marketplace')
            marketplace_list = cursor.fetchall()
            for p in marketplace_list:
                marketplaces.append(Marketplace(p[1], p[2], p[0]))
    except Exception as e:
        print(e)
    return marketplaces

def list_by_id(id: int) -> Marketplace:
    mkp = []
    try:
        with Connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM marketplace where id = {id}')
            marketplace = cursor.fetchone()
            mkp = Marketplace(marketplace[1],marketplace[2],marketplace[0])
    except Exception as e:
        print(e)
    return mkp

def update_marketplace(marketplace: Marketplace) -> None:
    try:
        with Connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE marketplace set name = '{marketplace.name}', description='{marketplace.description}' where id = '{marketplace.id}'")
            conn.commit()
    except Exception as e:
        print(e)

def del_marketplace(id: int) -> None:
    try:
        with Connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM marketplace where id = '{id}'")
            conn.commit()
    except Exception as e:
        print(e)