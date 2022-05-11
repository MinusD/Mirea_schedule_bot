import requests
from bs4 import BeautifulSoup
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import config


def main():
    vk_session = vk_api.VkApi(token=config.TOKEN)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text:
            print('New from {}, text = {}'.format(event.user_id, event.text))
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Привет, ' + vk.users.get(user_id=event.user_id)[0]['first_name']
            )


if __name__ == '__main__':
    main()
