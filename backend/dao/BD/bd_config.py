import psycopg2

_file_name = 'backend/files/credentials.txt'


def _get_credential() -> list:
    credentials = []
    with open(_file_name, 'r') as file:
        for line in file:
            l = line.strip()
            credentials.append(l)
    connection_string = f'host={credentials[0]} user={credentials[1]} dbname={credentials[2]} password={credentials[3]}'
    return connection_string


def connection_credentials() -> str:
    c_string = _get_credential()
    _generate_databases()
    return c_string

def _generate_databases():
    try:
        with psycopg2.connect(_get_credential()) as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS product (id serial not null, name varchar(200) not null, description varchar(200) not null, price numeric(20) not null, constraint product_pk primary key (id)) ;")
            cur.execute("CREATE TABLE IF NOT EXISTS category (id serial not null, name varchar(200) not null, description varchar(200) not null, constraint category_pk primary key (id)) ;")
            cur.execute("CREATE TABLE IF NOT EXISTS marketplace (id serial not null, name varchar(50) not null, description varchar(200) null, constraint marketplace_pk primary key (id));")
            cur.execute("CREATE TABLE IF NOT EXISTS seller (id serial not null, name varchar(100) not null, phone varchar(20) not null, mail varchar(50) not null, constraint seller_pk primary key (id));")
            cur.execute("CREATE TABLE IF NOT EXISTS log (id serial not null, datetime timestamp not null, action varchar(400) not null, constraint log_pk primary key (id));")
            conn.commit()
    except Exception as e:
        print(e)
