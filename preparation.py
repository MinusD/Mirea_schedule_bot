import os
import sys
import glob
import shutil

import src.cfgs.system_config as cfg
from src.sql_database import *

if __name__ == '__main__':
    app_path = os.path.dirname(os.path.realpath(sys.argv[0]))  # Папка, откуда запускаемся
    data_path = os.path.join(app_path, cfg.DATA_DIR[:-1])
    os.makedirs(data_path, exist_ok=True)
    open(cfg.DATA_DIR + cfg.DATABASE_FILENAME, 'w').close()
    open(cfg.DATA_DIR + cfg.LOG_FILENAME, 'w').close()
    db = Database()
    db.create_table(cfg.TABLE_NAME, [['user_id', 'INTEGER'], ['group_slug', 'VARCHAR(30)']])
    del db
