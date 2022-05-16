TOKEN: str = 'dfb468c2e5cf615a4c9f534eba0ded63bd20d15a4576743f1154f15ccf86bdd2296dc24e251d91117a043'
WEATHER_TOKEN: str = '483841295963b30a56e7679ae38f99e1'
MIREA_SCHEDULE_URL: str = 'https://www.mirea.ru/schedule/'
WEATHER_URL: str = 'https://api.openweathermap.org/data/2.5/weather?q=moscow&appid={}&units=metric&lang=ru'
CORONA_STAT_URL: str = 'https://coronavirusstat.ru'
DEBUG_MODE: bool = True
LOG_MODE: bool = True
UPDATE_SCHEDULE_FILE_ON_START: bool = False
ADMIN_VK_ID: int = 382889632
WEEK_DELTA: int = -5

GROUP_PATTERN: str = r'\w{4}-\d{2}-\d{2}'  # Паттерн группы

TABLE_NAME: str = 'groups'

LOG_FILENAME: str = 'log.txt'
DATABASE_FILENAME: str = 'vk_bot_data.db'
MAIN_DIR: str = 'src/'
DATA_DIR: str = 'data/'
SCHEDULE_BASE_NAME: str = 'schedule'
