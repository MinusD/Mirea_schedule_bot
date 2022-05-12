import datetime
from src.cfgs import system_config as cfg


class Log:
    def __init__(self, key: str = 'LOG', comment: str = '') -> None:
        if cfg.LOG_MODE:
            with open(cfg.DATA_DIR + cfg.LOG_FILENAME, 'a') as f:
                f.write(f'{key} --- {str(datetime.datetime.now())} --- {comment}\n')
                # f.write(f'{key} --- {str(datetime.datetime.now())[:-7]} --- {comment}\n')


class Debug:
    def __init__(self, data: any = '', is_log: bool = True, key: str = 'LOG'):
        if cfg.DEBUG_MODE:
            print(data)
        if cfg.LOG_MODE and is_log:
            with open(cfg.DATA_DIR + cfg.LOG_FILENAME, 'a') as f:
                f.write(f'{key} --- {str(datetime.datetime.now())} --- {data}\n')
                # f.write(f'{key} --- {str(datetime.datetime.now())[:-7]} --- {comment}\n')
