# Встроенные библиотеки
import requests
import time
import re
from bs4 import BeautifulSoup

# Сторонние библиотеки
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

# Самописные модули
from src.helper_module import *
from src.sql_database import *

import src.cfgs.main_config as cfg
import src.cfgs.system_config as scfg


class VkBot:
    def __init__(self) -> None:
        self.vk_session = vk_api.VkApi(token=scfg.TOKEN)
        self.vk = self.vk_session.get_api()
        self.longpoll = VkLongPoll(self.vk_session)
        self.users_to_set_group: set = set()
        self.last_schedule_file_update: time
        self._update_schedule_file()
        Debug('Bot init', key='SRT')

        # self.users_to_set_group.add('707879525')

    # Начинаем слушать ивенты
    def start_listen(self) -> None:
        Debug('Start listen', key='SRT')
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
                Debug('from {} text = \'{}\''.format(event.user_id, event.text), key='MSG')
                self._command_handler(event.user_id, event.text.lower())

    # Добавляет пользователя в список обновления группы
    def _add_user_to_edit_group_list(self, user_id):
        self.users_to_set_group.add(str(user_id))
        Debug(f'User add to set group list, uid: {user_id}', key='SET')

    # Обработчик команд
    def _command_handler(self, user_id: int, text: str) -> None:
        match text:
            case cfg.CMD_START:
                user_data = self.vk.users.get(user_id=user_id)[0]
                self._send_message(user_id, cfg.ABOUT_TEXT.format(user_data['first_name']))
                Debug(f'Start new user: {user_data["first_name"]} {user_data["last_name"]}')
                self._add_user_to_edit_group_list(user_id)
                return

        if str(user_id) in self.users_to_set_group:
            self._edit_user_group(user_id, text)
            return
        self._send_message(user_id, cfg.INVALID_COMMAND_TEXT)
        # print(self.users_to_set_group)

    def _edit_user_group(self, user_id: int, group_slug: str) -> None:
        group_pattern = r'\w{4}-\d{2}-\d{2}'  # Паттерн группы
        group_slug = group_slug.upper()
        if re.match(group_pattern, group_slug):
            db = Database()
            if not db.fetch_one(table=scfg.TABLE_NAME, condition=f'user_id = {user_id}'):
                db.insert_one(table=scfg.TABLE_NAME, data=[user_id, group_slug])
                Debug(f'Set user group: {group_slug} uid: {user_id}', key='SET')
            else:
                db.update_one(table=scfg.TABLE_NAME, sets=f'group_slug = \'{group_slug}\'',
                              condition=f'user_id = {user_id}')
                Debug(f'ReSet user group: {group_slug} uid: {user_id}', key='RST')
            self._send_message(user_id, cfg.SET_GROUP_TEXT.format(group_slug), 1)
            self._clear_wait_lists(user_id)  # Убираем из списка ожидания
        else:
            self._send_message(user_id, cfg.INVALID_GROUP_TEXT)
            Debug(f'Invalid group format {group_slug} uid: {user_id}', key='INV')
        # Debug('from {} text = \'{}\''.format(event.user_id, event.text), key='MSG')
        # self._command_handler(event.user_id, event.text.lower())

    # Убирает пользователя из списка ожидания
    def _clear_wait_lists(self, user_id: int) -> None:
        self.users_to_set_group.discard(str(user_id))

    def _send_message(self, user_id: int, text: str, keyboard: int = 0):
        """
        Отправка сообщения
        :param user_id:
        :param text:
        :param keyboard: 0 - Без клавиатуры(не менять), 1 - Стандартная клавиатура, 2 - Дополнительная(Настройки)
        :return:
        """
        if keyboard == 1:
            keyboard = VkKeyboard(one_time=False)
            keyboard.add_button('Начать', color=VkKeyboardColor.NEGATIVE)
            keyboard.add_line()  # переход на вторую строку
            keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)
        elif keyboard == 2:
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('321', color=VkKeyboardColor.NEGATIVE)
            keyboard.add_line()  # переход на вторую строку
            keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)
        if keyboard:
            self.vk.messages.send(
                user_id=user_id,
                random_id=get_random_id(),
                keyboard=keyboard.get_keyboard(),
                message=text
            )
        else:
            self.vk.messages.send(
                user_id=user_id,
                random_id=get_random_id(),
                message=text
            )

    def _update_schedule_file(self) -> None:
        """
        Обновляет файл с расписанием

        :return:
        """
        page = requests.get(scfg.MIREA_SCHEDULE_URL)  # Получаем страницу
        soup = BeautifulSoup(page.text, "html.parser")  # Парсим её
        result = soup.find(string="Институт информационных технологий").find_parent("div").find_parent("div").findAll(
            'a', {'class': 'uk-link-toggle'})
        course_pattern = r'([1-3]) курс'
        for x in result:
            course = x.find('div', 'uk-link-heading').text.lower().strip()
            cf = re.match(course_pattern, course)
            if cf:
                cf = cf.group(1)
                f = open(f'{scfg.DATA_DIR}{scfg.SCHEDULE_BASE_NAME}{cf}.xlsx', "wb")
                link = x.get('href')
                resp = requests.get(link)  # запрос по ссылке
                f.write(resp.content)  # Записываем контент в файл
        self.last_schedule_file_update = time.time()
        # match course:
        #     case '1 курс':
        #
        # if  == '1 курс':
        #     f = open("file.xlsx", "wb")
        #     link = x.get('href')
        #     resp = requests.get(link)  # запрос по ссылке
        #     f.write(resp.content)


def main():
    bot = VkBot()
    bot.start_listen()


if __name__ == '__main__':
    main()
