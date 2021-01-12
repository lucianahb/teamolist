import psycopg2

host = 'pgsql08-farm15.uni5.net'
user = 'topskills1'
password = 'olist21'
database = 'topskills1'

def generate_connection_string():
    connection_string = f"host={host} user={user} dbname={database} password={password}"
    return connection_string