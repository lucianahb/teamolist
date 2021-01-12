import psycopg2
from backend.dao.BD.bd_config import generate_connection_string
from backend.models.marketplace import Marketplace


def create_mkplace(marketplace: Marketplace):
    try:
        conn = psycopg2.connect(generate_connection_string())
        cursor = conn.cursor()
        query = f"INSERT INTO marketplace (name, description) VALUES ('{marketplace.name}', '{marketplace.description}');"
        cursor.execute(query)
        conn.commit()
        
    except Exception as e:
        print("deu ruim")
        print(e)

    finally:
        pass
        cursor.close()
        conn.close()



def read_mkplaces()->list:
    try:
        marketplaces = []
        conn = psycopg2.connect(generate_connection_string())
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM marketplace')

        marketplace_list = cursor.fetchall()

        for p in marketplace_list:
            marketplaces.append(Marketplace(p[1], p[2], p[0]))
        
        return marketplaces
    except Exception as e:
        print(e)

    finally:
        conn.close()
