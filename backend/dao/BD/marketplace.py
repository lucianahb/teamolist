from backend.dao.BD.bd_config import generate_connection
from backend.models.marketplace import Marketplace


def create_mkplace(marketplace: Marketplace) -> None:
    conn = generate_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO marketplace (name, description) VALUES ('{marketplace.name}', '{marketplace.description}');"
    cursor.execute(query)
    conn.commit()
    
    cursor.close()
    conn.close()


def read_mkplaces()->list:
    marketplaces = []
    conn = generate_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM marketplace')
    marketplace_list = cursor.fetchall()
    for p in marketplace_list:
        marketplaces.append(Marketplace(p[1], p[2], p[0]))
    
    cursor.close()
    conn.close()
    return marketplaces
        
