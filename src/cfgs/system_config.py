TOKEN: str = ''
MIREA_SCHEDULE_URL: str = 'https://www.mirea.ru/schedule/'
CORONA_STAT_URL: str = 'https://coronavirusstat.ru'
DEBUG_MODE: bool = True  # Выводит действия
LOG_MODE: bool = True  # Логирует ключевые действия
UPDATE_SCHEDULE_FILE_ON_START: bool = True  # Запрашивать ли расписания с сайта при запуске
WEEK_DELTA: int = -5  # Номер учебной недели по сравнению с неделей в году

GROUP_PATTERN: str = r'\w{4}-\d{2}-\d{2}'  # Паттерн группы

TABLE_NAME: str = 'groups'

GRAF_FILENAME = 'graf.png'
WEATHER_PATTERN_FILENAME = 'weather_pattern.jpg'
LOG_FILENAME: str = 'log.txt'
DATABASE_FILENAME: str = 'vk_bot_data.db'
MAIN_DIR: str = 'src/'
DATA_DIR: str = 'data/'
SCHEDULE_BASE_NAME: str = 'schedule'
