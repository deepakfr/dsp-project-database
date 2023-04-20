import psycopg2

host = 'localhost'
db = 'Hr_Job_Change'
password = '1234'
port = 5432
user = 'postgres'

try:
    conn = psycopg2.connect(
        host=host,
        database=db,
        password=password,
        port=port,
        user=user
    )


    cur = conn.cursor()

    print("Database connected")

    # TODO: execute SQL commands or queries here

    conn.commit()
except psycopg2.Error as error:
    print('Error connecting to the PostgreSQL database:', error)
finally:
    if 'cur' in locals() and cur is not None:
        cur.close()
    if 'conn' in locals() and conn is not None:
        conn.close()