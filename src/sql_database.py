# import psycopg2
import sqlite3 as sql
import src.cfgs.system_config as scfg


class Database:
    def __init__(self) -> None:
        self.conn = sql.connect(scfg.DATA_DIR + scfg.DATABASE_FILENAME)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name: str, columns: [[int, str]]) -> None:
        req = 'CREATE TABLE {}({});'.format(table_name, ', '.join([(str(x[0]) + " " + x[1]) for x in columns]))
        self.cursor.execute(req)

    def fetch_one(self, columns: str = '*', table: str = '', condition: str = '') -> any:
        req = 'SELECT {} FROM {} WHERE {} LIMIT 1'.format(columns, table, condition)
        return self.cursor.execute(req).fetchone()

    def insert_one(self, table: str = '', data: list = []) -> any:
        req = 'INSERT INTO {} VALUES ({})'.format(table,
                                                  ', '.join([(str(x) if type(x) == int else f'\'{x}\'') for x in data]))
        self.cursor.execute(req)
        self.conn.commit()

    def update_one(self, table: str = '', sets: str = '', condition: str = '') -> None:
        req = 'UPDATE {} SET {} WHERE {}'.format(table, sets, condition)
        self.cursor.execute(req)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
# conn = sql.connect(cfg.DATABASE_FILENAME)
# cursor = conn.cursor()
# print(cursor)
