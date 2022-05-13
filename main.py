# Встроенные библиотеки
import datetime
import openpyxl
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
        self.schedule_data: list
        self._update_schedule_file()

        Debug('Bot init', key='SRT')

    def start_listen(self) -> None:
        """
        Слушатель событий вк

        :return:
        """
        Debug('Start listen', key='SRT')
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
                Debug('from {} text = \'{}\''.format(event.user_id, event.text), key='MSG')
                self._command_handler(event.user_id, event.text.lower())

    def _add_user_to_edit_group_list(self, user_id) -> None:
        """
        Добавляет пользователя в список обновления группы

        :param user_id:
        :return:
        """
        self.users_to_set_group.add(str(user_id))
        Debug(f'User add to set group list, uid: {user_id}', key='SET')

    def _command_handler(self, user_id: int, text: str) -> None:
        """
        Обработчик команд

        :param user_id:
        :param text:
        :return:
        """
        match text:
            case cfg.CMD_START:
                user_data = self.vk.users.get(user_id=user_id)[0]
                self._send_message(user_id, cfg.ABOUT_TEXT.format(user_data['first_name']))
                Debug(f'Start new user: {user_data["first_name"]} {user_data["last_name"]}')
                self._add_user_to_edit_group_list(user_id)
                return
            case cfg.CMD_SCHEDULE:
                self._show_schedule_keyboard(user_id)
                return
            case cfg.BTN_SCHEDULE_TODAY:

                return
            case cfg.BTN_WHAT_WEEK:
                self._show_current_week(user_id)
            case cfg.BTN_WHAT_GROUP:
                self._show_user_group(user_id)
                return

        if str(user_id) in self.users_to_set_group:
            self._edit_user_group(user_id, text)
            return
        self._send_message(user_id, cfg.INVALID_COMMAND_TEXT.format(cfg.BTN_HELP))

    def _get_user_group(self, user_id: int) -> str or None:
        """
        Получает группу пользователя или ошибка

        :param user_id:
        :return: Номер группы или None
        """
        group = Database().fetch_one(table=scfg.TABLE_NAME, condition=f'user_id = {user_id}')
        if group:
            return group[1]
        return None

    def _get_current_week(self) -> int:
        """
        Возвращает номер текущей недели

        :return: учебная неделя
        """
        return datetime.datetime.now().isocalendar().week + scfg.WEEK_DELTA

    def _show_current_week(self, user_id: int) -> None:
        """
        Выводит пользователю номер текущей недели

        :param user_id:
        :return:
        """
        self._send_message(user_id, cfg.CURRENT_WEEK_TEXT.format(self._get_current_week()))

    def _show_user_group(self, user_id: int) -> None:
        """
        Выводит пользователю номер выбранной группы или ошибку

        :param user_id:
        :return:
        """
        group = self._get_user_group(user_id)
        if group:
            self._send_message(user_id, cfg.CURRENT_GROUP_TEXT.format(group))
        else:
            self._send_message(user_id, cfg.CURRENT_GROUP_ERROR_TEXT.format(cfg.CMD_SCHEDULE.title()))

    def _show_schedule_keyboard(self, user_id: int) -> None:
        """
        Показать клавиатуру выбора расписания

        :param user_id:
        :return:
        """
        Debug(f'Show schedule keyboard for id: {user_id}')
        self._send_message(user_id, cfg.SCHEDULE_SELECT_TEXT, keyboard=1)

    def _edit_user_group(self, user_id: int, group_slug: str) -> None:
        """
        Изменить группу пользователя или выдать ошибку

        :param user_id:
        :param group_slug:
        :return:
        """
        group_slug = group_slug.upper()
        if self._validate_group_slug(group_slug):
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
            self._show_schedule_keyboard(user_id=user_id)  # Показываем клавиатуры выбора
            del db
        else:
            self._send_message(user_id, cfg.INVALID_GROUP_TEXT)
            Debug(f'Invalid group format {group_slug} uid: {user_id}', key='INV')

        # Debug('from {} text = \'{}\''.format(event.user_id, event.text), key='MSG')
        # self._command_handler(event.user_id, event.text.lower())

    def _clear_wait_lists(self, user_id: int) -> None:
        """
        Убирает пользователя из списка ожидания

        :param user_id:
        :return:
        """
        self.users_to_set_group.discard(str(user_id))

    def _validate_group_slug(self, group_slug: str) -> bool:
        """
        Проверка на валидность номера группы по маске и списку групп

        :param group_slug:
        :return:
        """
        group_slug = group_slug.upper()
        if re.match(scfg.GROUP_PATTERN, group_slug):
            year_of_in = int('20' + group_slug[-2:])
            now = datetime.datetime.now()
            if now.month <= 6:
                year_of_in += 1
            course_number = now.year - year_of_in  # Курс - 1
            if time.time() - 43200 > self.last_schedule_file_update:  # Если с последнего обновления > 12 часов
                self._update_schedule_file()
            if 0 <= course_number <= 2:
                for i in range(0, len(self.schedule_data[course_number]), 4):
                    if self.schedule_data[course_number][i][0] == group_slug:
                        Debug(f'Find in file group: {group_slug} column: {i + 1}', key='FND')
                        return True
        return False

    def _send_message(self, user_id: int, text: str, keyboard: int = 0) -> None:
        """
        Отправка сообщения

        :param user_id: ID пользователя
        :param text: Текс сообщения
        :param keyboard: 0 - Без клавиатуры(не менять), 1 - Стандартная клавиатура, 2 - Дополнительная(Настройки)
        :return:
        """
        if keyboard == 1:
            keyboard = VkKeyboard(one_time=False)
            keyboard.add_button(cfg.BTN_SCHEDULE_TODAY, color=VkKeyboardColor.POSITIVE)
            keyboard.add_button(cfg.BTN_SCHEDULE_TOMORROW, color=VkKeyboardColor.NEGATIVE)
            keyboard.add_line()
            keyboard.add_button(cfg.BTN_SCHEDULE_WEEK, color=VkKeyboardColor.PRIMARY)
            keyboard.add_button(cfg.BTN_SCHEDULE_NEXT_WEEK, color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button(cfg.BTN_WHAT_WEEK.title(), color=VkKeyboardColor.SECONDARY)
            keyboard.add_button(cfg.BTN_WHAT_GROUP.title(), color=VkKeyboardColor.SECONDARY)
            keyboard.add_button(cfg.BTN_HELP.title(), color=VkKeyboardColor.SECONDARY)
            keyboard.add_button(cfg.BTN_SETTINGS.title(), color=VkKeyboardColor.SECONDARY)

            # keyboard.add_button('Начать', color=VkKeyboardColor.NEGATIVE)
            # keyboard = VkKeyboard(one_time=True)
            #   # переход на вторую строку
            # keyboard.add_button('ИКБО-30-21', color=VkKeyboardColor.POSITIVE)
            # keyboard.add_button('ИКБО-10-21', color=VkKeyboardColor.POSITIVE)
            # keyboard.add_button('ИКБО-00-21', color=VkKeyboardColor.POSITIVE)
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
            course_number = re.match(course_pattern, course)
            if course_number:
                course_number = course_number.group(1)
                f = open(f'{scfg.DATA_DIR}{scfg.SCHEDULE_BASE_NAME}{course_number}.xlsx', "wb")
                link = x.get('href')
                resp = requests.get(link)  # запрос по ссылке
                f.write(resp.content)  # Записываем контент в файл
                f.close()
        self.last_schedule_file_update = time.time()
        Debug('Update schedule files', key='UPD')
        self._parse_schedule_file()

    def _parse_schedule_file(self) -> None:
        """
        Парсит полученные файлы расписание и записывает в списки

        :return:
        """
        self.schedule_data = []
        for c in range(3):
            data_tmp = []
            book = openpyxl.load_workbook(
                f'{scfg.DATA_DIR}{scfg.SCHEDULE_BASE_NAME}{c + 1}.xlsx')  # открытие файла
            sheet = book.active  # активный лист
            num_cols = sheet.max_column  # количество столбцов
            num_rows = sheet.max_row  # количество строк
            last_group_cell = 0  # Сколько прошло ячеек от последней группы
            for i in range(6, num_cols):
                if last_group_cell >= 4:  # Если после группы прошло 4 ячейки, ждём следующей группы
                    last_group_cell = -1
                    continue
                column = []
                for j in range(2, 75):  # Перебираем
                    v = str(sheet.cell(column=i, row=j).value)
                    if j == 2 and re.match(scfg.GROUP_PATTERN,
                                           v):  # Если ячейка вторая, то проверяем что это номер группы
                        last_group_cell = 0  # Если это так, обнуляем счётчик
                    column.append(v)
                if last_group_cell != -1:  # Пока не дошли до следующей группы, не добавляем столбцы,
                    data_tmp.append(column)
                    last_group_cell += 1
            self.schedule_data.append(data_tmp)
        Debug('Parse schedule file', key='PRS')


def main():
    bot = VkBot()
    bot.start_listen()


if __name__ == '__main__':
    main()
