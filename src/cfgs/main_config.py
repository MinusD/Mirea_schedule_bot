CMD_START = 'начать'
CMD_SCHEDULE = 'бот'
CMD_FIND_TEACHER = 'найти'
CMD_CORONA = 'корона'

SPLIT_PAIR_SEPARATOR = ' / '
WINDOW_SIGNATURE = '--'
VOID_SIGNATURE = '_'
ONE_PAIR_PATTERN = '{}) {}, {}, {}, {}\n'  # Номер, Предмет, Тип, Преподаватель, Аудитория
ONE_PAIR_SHORT_PATTERN = '{}) {}\n'
ONE_DAY_HEADER_PATTERN = '\nРасписание на {}:\n'  #
ONE_DAY_TEACHER_HEADER_PATTERN = '\nРасписание преподавателя {} на {}:\n'  #

ODD_DAY_PATTERN = 'Расписание на {}, нечётной недели\n'
EVEN_DAY_PATTERN = 'Расписание на {} чётной недели\n'

MONTHS_SLUGS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                'ноября', 'декабря']
WEEK_DAYS_SLUGS = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье']
WEEK_DAYS_INFINITIVE_SLUGS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

ABOUT_TEXT = 'Привет {}!\nЯ бот, который поможет посмотреть расписание, а так же покажет другую ' \
             'полезную информацию\n\n' \
             'Для начала напиши номер своей группы, а я её запомню, что бы больше не приходилось её указывать\n\n'
INVALID_GROUP_TEXT = 'Неверный формат или группа не найдена!\n\nФормат: \'АБВГ-12-34\''
SET_GROUP_TEXT = 'Я запомнил, что ты учишься в группе {}'
CURRENT_GROUP_TEXT = 'Я показываю расписание группы {}'
CURRENT_GROUP_ERROR_TEXT = 'Группа не выбрана, для выбора группы, напишите \n\'{}\' и номер группы'
CURRENT_WEEK_TEXT = 'Идёт {} неделя'
SCHEDULE_SELECT_TEXT = 'Показать расписание ...'
TEACHER_SELECT_TEXT = 'Выберите преподавателя'
TEACHER_SELECT_PERIOD_TEXT = 'Показать расписание преподавателя {} ...'
TEACHER_SELECT_ERROR_TEXT = 'Преподаватель не найден'

INVALID_COMMAND_TEXT = 'Неизвестная команда\nЧто бы получить список команд напиши \'{}\''
HELP_TEXT = 'Нам никто не поможет :/'

BTN_SCHEDULE_TODAY = 'на сегодня'
BTN_SCHEDULE_TOMORROW = 'на завтра'
BTN_SCHEDULE_WEEK = 'на эту неделю'
BTN_SCHEDULE_NEXT_WEEK = 'на следующую неделю'
BTN_WHAT_WEEK = 'неделя?'  # 'Какая неделя?'
BTN_WHAT_GROUP = 'группа?'  # 'Какая группа?'
BTN_SETTINGS = 'настройки'
BTN_HELP = 'помощь'
