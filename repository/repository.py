import psycopg2
from loguru import logger

class Repository:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=ys-db user=ys-user password=qwerty port=5432")
        logger.debug("connected to database")

    def insert_link(self, s: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute("insert into links (link) \
                        values (%s) returning id", (s,))
        id = cursor.fetchone()
        # logger.debug(f"id = {id}")
        self.conn.commit()
        cursor.close()
        return id
    
    def insert_code(self, code: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute("insert into codes (code) \
                       values (%s) returning id", (code,))
        id = cursor.fetchone()
        self.conn.commit()
        cursor.close()
        return id
    
    def insert_link_to_code(self, link_id: int, code_id: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute("insert into link_to_code (link_id, code_id) \
                       values (%s, %s)", (link_id, code_id,))
        self.conn.commit()
        cursor.close()

    def select_link(self, code: str) -> str:
        cursor = self.conn.cursor()
        cursor.execute("select l.link from links l \
                       left join link_to_code lc on lc.link_id = l.id \
                       left join codes c on lc.code_id = c.id \
                       where c.code = %s", (code,))
        data = cursor.fetchone()
        link = ""
        if data == None:
            logger.debug("link doesn't found")
        else:
            link = data[0]
        self.conn.commit()
        cursor.close()
        return link
    
    def exists_code(self, code: str) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("select exists(select 1 from codes where code = %s)", (code,))
        val = cursor.fetchone()
        if val == None:
            logger.debug("something went wrong in exists query")
        self.conn.commit()
        cursor.close()
        return val[0]
    
    def reinit(self) -> None:
        """ Migrations """
        cursor = self.conn.cursor()
        cursor.execute(open('schema.sql', 'r').read())
        self.conn.commit()
        cursor.close()

    def close_db(self) -> None:
        self.conn.close()
        logger.debug("connection closed")
