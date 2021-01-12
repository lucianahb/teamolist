import psycopg2

root = 'backend/files/list_marketplace.txt'
host = "pgsql08-farm15.uni5.net"
user = "topskills1"
password = "olist21"
database = "topskills1"
connection_string = f"host={host} dbname={database} user={user} password={password}"

def create_mkplace(name:str, description:str):
    try:
        conn = psycopg2.connect(connection_string)
        
        with conn.cursor() as cur:
            cur.execute(f'''
            INSERT INTO markeplace (name, description) VALUES ('{name}', '{description}');
            ''')

        conn.commit()
    except Exception as e:
        print("deu ruim")
        print(e)

    finally:
        pass
        conn.close()



def read_mkplaces()->list:
    try:
        conn = psycopg2.connect(connection_string)
        
        with conn.cursor() as cur:
            cur.execute('select * from markeplace')
            
            result = cur.fetchall()
            print("result" + str(result))
            return result
    except Exception as e:
        print(e)

    finally:
        conn.close()
