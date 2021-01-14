import psycopg2

class Connection:
    __file_name = 'backend/files/credentials.txt'

    def __get_credential(self) -> list:
        credentials = []
        with open(self.__file_name, 'r') as file:
            for line in file:
                l = line.strip()
                credentials.append(l)
        connection_string = f'host={credentials[0]} user={credentials[1]} dbname={credentials[2]} password={credentials[3]}'
        return connection_string

    def __generate_databases(self):
        try:
            with psycopg2.connect(self.__get_credential()) as conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS product (id serial not null, name varchar(200) not null, description varchar(200) not null, price numeric(20) not null, constraint product_pk primary key (id)) ;")
                cur.execute("CREATE TABLE IF NOT EXISTS category (id serial not null, name varchar(200) not null, description varchar(200) not null, constraint category_pk primary key (id)) ;")
                cur.execute("CREATE TABLE IF NOT EXISTS marketplace (id serial not null, name varchar(50) not null, description varchar(200) null, constraint marketplace_pk primary key (id));")
                cur.execute("CREATE TABLE IF NOT EXISTS seller (id serial not null, name varchar(100) not null, phone varchar(20) not null, mail varchar(50) not null, constraint seller_pk primary key (id));")
                cur.execute("CREATE TABLE IF NOT EXISTS log (id serial not null, datetime timestamp not null, action varchar(400) not null, constraint log_pk primary key (id));")
                conn.commit()
        except Exception as e:
            print(e)
    
    def __enter__(self):
        self.__generate_databases()
        self.__connection = psycopg2.connect(self.__get_credential())
        return self.__connection

    def __exit__(self, type, value, trace):
        self.__connection.close()
