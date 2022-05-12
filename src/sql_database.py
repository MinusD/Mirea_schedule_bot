# import psycopg2
import sqlite3 as sql
import src.cfgs.main_config as cfg


class Database:
    def __init__(self):
        self.conn = sql.connect(cfg.MAIN_DIR + cfg.DATABASE_FILENAME)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name: str):
        self.cursor.execute(f'CREATE TABLE {table_name}')

# conn = sql.connect(cfg.DATABASE_FILENAME)
# cursor = conn.cursor()
# print(cursor)
