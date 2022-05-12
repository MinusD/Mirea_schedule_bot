# Встроенные библиотеки
import requests
from bs4 import BeautifulSoup
# Сторонние библиотеки
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

# Самописные модули
import src.cfgs.main_config as cfg


def main():
    vk_session = vk_api.VkApi(token=cfg.TOKEN)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and event.text == 'Начать':
            print('New from {}, text = {}'.format(event.user_id, event.text))
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Привет, ' + vk.users.get(user_id=event.user_id)[0]['first_name']
            )
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Начать', color=VkKeyboardColor.NEGATIVE)
            keyboard.add_line()  # переход на вторую строку
            keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                keyboard=keyboard.get_keyboard(),
                message='Пример клавиатуры'
            )
            # break


if __name__ == '__main__':
    main()
