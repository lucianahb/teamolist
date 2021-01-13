from backend.dao.BD.bd_config import connection_credentials
from backend.models.marketplace import Marketplace
import psycopg2


def create_mkplace(marketplace: Marketplace) -> None:
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            query = f"INSERT INTO marketplace (name, description) VALUES ('{marketplace.name}', '{marketplace.description}');"
            cursor.execute(query)
            conn.commit()
    except Exception as e:
        print(e)


def read_mkplaces()->list:
    marketplaces = []
    try:
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM marketplace')
            marketplace_list = cursor.fetchall()
            for p in marketplace_list:
                marketplaces.append(Marketplace(p[1], p[2], p[0]))
    except Exception as e:
        print(e)
    return marketplaces
        
