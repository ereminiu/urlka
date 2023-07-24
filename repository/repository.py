import psycopg2
from loguru import logger

class Repository:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=ys-db user=ys-user password=qwerty port=5432")
        logger.debug("connected to database")

    def reinit(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute(open('schema.sql', 'r').read())
        cursor.close()

    def close_db(self) -> None:
        self.conn.close()
        logger.debug("connection closed")