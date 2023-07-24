import psycopg2

class Repository:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=ys-db user=ys-user password=qwerty port=5432")
    
    def close_db(self) -> None:
        self.conn.close()