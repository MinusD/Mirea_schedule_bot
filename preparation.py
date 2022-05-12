import src.cfgs.main_config as cfg
import src.cfgs.vk_config as vkcfg
from src.sql_database import *

if __name__ == '__main__':
    dir = 'src/'
    open(dir + cfg.DATABASE_FILENAME, 'w').close()
    open(dir + vkcfg.LOG_FILENAME, 'w').close()
