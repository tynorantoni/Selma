import psycopg2
from support.credentials import read_credentials



#after creating DB commands will be configured
DB_INIT_COMMANDS =(
    """
    CREATE SCHEMA IF NOT EXISTS selma_db
    """,
    """
    CREATE TABLE IF NOT EXISTS table1 (
            name_id SERIAL PRIMARY KEY,
            table_name VARCHAR(255) NOT NULL
        )
    """,
    """
    CREATE TABLE IF NOT EXISTS table2 (
            table2_id SERIAL PRIMARY KEY,
            table2_name VARCHAR(255) NOT NULL,
            table2_number INTEGER,
            table2_value BOOL NOT NULL
        )
    """
)

def connect_to_db():
    db_credentials = read_credentials()
    print(db_credentials)
    conn = psycopg2.connect(
        host=db_credentials['host'],
        port=db_credentials['port'],
        database=db_credentials['database'],
        user=db_credentials['user'],
        password=db_credentials['password']
    )
    return conn

def create_tables_in_db():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        for command in DB_INIT_COMMANDS:
            cursor.execute(command)
        
        cursor.close()
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as err:
        print(err)
    finally:
        if connection is not None:
            connection.close()