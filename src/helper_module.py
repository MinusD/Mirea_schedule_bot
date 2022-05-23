import datetime
import src.cfgs.system_config as scfg


class Log:
    def __init__(self, key: str = 'LOG', comment: str = '') -> None:
        if scfg.LOG_MODE:
            with open(scfg.DATA_DIR + scfg.LOG_FILENAME, 'a') as f:
                f.write(f'{key} --- {str(datetime.datetime.now())} --- {comment}\n')


class Debug:
    def __init__(self, data: any = '', is_log: bool = True, key: str = 'LOG'):
        if scfg.DEBUG_MODE:
            print(data)
        if scfg.LOG_MODE and is_log:
            with open(scfg.DATA_DIR + scfg.LOG_FILENAME, 'a') as f:
                f.write(f'{key} --- {str(datetime.datetime.now())} --- {data}\n')
