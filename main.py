# Встроенные библиотеки
import requests
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
        Debug('Bot init', key='SRT')

        self.users_to_set_group.add('707879525')

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
                db.update_one(table=scfg.TABLE_NAME, sets=f'group_slug = \'{group_slug}\'', condition=f'user_id = {user_id}')
        else:
            self._send_message(user_id, cfg.INVALID_GROUP_TEXT)
        print(group_slug)
        # Debug('from {} text = \'{}\''.format(event.user_id, event.text), key='MSG')
        # self._command_handler(event.user_id, event.text.lower())

    # Убирает пользователя из списка ожидания
    def _clear_wait_lists(self, user_id):
        self.users_to_set_group.discard(user_id)

    def _send_message(self, user_id: int, text: str):
        self.vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=text
        )


def main():
    bot = VkBot()
    bot.start_listen()
    # vk_session = vk_api.VkApi(token=cfg.TOKEN)
    # vk = vk_session.get_api()
    # longpoll = VkLongPoll(vk_session)
    # for event in longpoll.listen():
    #     if event.type == VkEventType.MESSAGE_NEW and event.text and event.text == 'Начать':
    #         print('New from {}, text = {}'.format(event.user_id, event.text))
    #         vk.messages.send(
    #             user_id=event.user_id,
    #             random_id=get_random_id(),
    #             message='Привет, ' + vk.users.get(user_id=event.user_id)[0]['first_name']
    #         )
    #         keyboard = VkKeyboard(one_time=True)
    #         keyboard.add_button('Начать', color=VkKeyboardColor.NEGATIVE)
    #         keyboard.add_line()  # переход на вторую строку
    #         keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)
    #         vk.messages.send(
    #             user_id=event.user_id,
    #             random_id=get_random_id(),
    #             keyboard=keyboard.get_keyboard(),
    #             message='Пример клавиатуры'
    #         )
    #         # break


if __name__ == '__main__':
    main()
