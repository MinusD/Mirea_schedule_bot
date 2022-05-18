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

# Баг с конфигами

CMD_START = 'начать'
CMD_SCHEDULE = 'бот'
CMD_FIND_TEACHER = 'найти'
CMD_CORONA = 'корона'
CMD_WEATHER = 'погода'

SPLIT_PAIR_SEPARATOR = ' / '
WINDOW_SIGNATURE = '--'
VOID_SIGNATURE = '_'
ONE_PAIR_PATTERN = '{}) {}, {}, {}, {}\n'  # Номер, Предмет, Тип, Преподаватель, Аудитория
ONE_PAIR_SHORT_PATTERN = '{}) {}\n'
ONE_DAY_HEADER_PATTERN = '\nРасписание на {}:\n'  #
ONE_DAY_TEACHER_HEADER_PATTERN = '\nРасписание преподавателя {} на {}:\n'  #
CORONA_STATS_PATTERN = '{}\n\nРегион: {}\nСлучаев: {} ({} за сегодня)\nАктивных: {} ({} за сегодня)\n' \
                       'Вылечено: {} ({} за сегодня)\nУмерло: {} ({} за сегодня)'
CORONA_REGION_DEFAULT = 'Не найден, поэтому Россия'

ODD_DAY_PATTERN = 'Расписание на {}, нечётной недели\n'
EVEN_DAY_PATTERN = 'Расписание на {} чётной недели\n'

MONTHS_SLUGS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                'ноября', 'декабря']
WEEK_DAYS_SLUGS = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье']
WEEK_DAYS_INFINITIVE_SLUGS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

ABOUT_TEXT = 'Привет {}!\nЯ бот, который поможет посмотреть расписание, а так же покажет другую ' \
             'полезную информацию\n\n' \
             'Для начала напиши номер своей группы, а я её запомню, чтобы больше не приходилось её указывать\n\n'
INVALID_GROUP_TEXT = 'Неверный формат или группа не найдена!\n\nФормат: \'АБВГ-12-34\''
SET_GROUP_TEXT = 'Я запомнил, что ты учишься в группе {}'
CURRENT_GROUP_TEXT = 'Я показываю расписание группы {}'
CURRENT_GROUP_ERROR_TEXT = 'Группа не выбрана, для выбора группы, напишите \n\'{}\' и номер группы'
CURRENT_WEEK_TEXT = 'Идёт {} неделя'
SCHEDULE_SELECT_TEXT = 'Показать расписание ...'
TEACHER_SELECT_TEXT = 'Выберите преподавателя'
TEACHER_SELECT_PERIOD_TEXT = 'Показать расписание преподавателя {} ...'
TEACHER_SELECT_ERROR_TEXT = 'Преподаватель не найден'
GRAF_HEADER_TEXT = 'Россия - Детальная статистика - коронавирус'
GRAF_LABEL_TEXT = 'Количество - Миллионы'

INVALID_COMMAND_TEXT = 'Неизвестная команда\nЧто бы получить список команд напиши \'{}\''

BTN_SCHEDULE_TODAY = 'на сегодня'
BTN_SCHEDULE_TOMORROW = 'на завтра'
BTN_SCHEDULE_WEEK = 'на эту неделю'
BTN_SCHEDULE_NEXT_WEEK = 'на следующую неделю'
BTN_WHAT_WEEK = 'неделя?'
BTN_WHAT_GROUP = 'группа?'
BTN_SETTINGS = 'настройки'
BTN_HELP = 'помощь'

HELP_TEXT = 'Список команд:\n\nНачать - Запускает бота\nБот - Показывает клавиатуру для выбора периода расписания\n' \
            'Бот <номер группы> - Запоминает группу и показывает клавиатуру\n' \
            'Бот <день недели> - Показывает расписание на чётный и не чётный день\n' \
            'Бот <день недели> <номер группы> - Сохраняет группу и показывает расписание на день\n\n' \
            'Найти <фамилия преподавателя> [И.О.] - Получить расписание преподавателя за определённый период\n\n' \
            '<> - Обязательные аргументы\n[] - По желанию\n\n\n' \
            'P.S. Бот писался как домашнее задания по Ознакомительной практике, поэтому функционал ограничен, ' \
            'команды работают только для первых трёх курсов ИИТ, а так же, могут присутствовать баги, т.к. ' \
            'проводилось только ' \
            'alpha тестирование. Если нашли баг, [id382889632|напишите администратору].\n\nУдобный сайт с расписание:' \
            ' https://mbc-d.ru/schedule'
