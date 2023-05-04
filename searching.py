from tokens import com_token, user_token
from datetime import datetime

import vk_api
import requests
from Bot_db import *
from main import get_profile_info, user_validator, write_msg, users_search, photos_get
from vk_api.longpoll import VkLongPoll, VkEventType

class Searching():

    if __name__ == '__main__':
        vk_interface = vk_api.VkApi(token=com_token)
        longpoll = VkLongPoll(vk_interface)
        tools = VkTools(user_token)
        info_for_search = None
        offset = 0

            def search_profile(self, user_id, vk_interface, info_for_search):
                users = self.users_search(info_for_search)
                user = users.pop()
                photos = self.photos_get(user['id'])
                if photos:
                    write_msg(vk_interface, user_id,
                        f'Страница пользователя {user["first_name"]} {user["last_name"]}')
                    write_msg(vk_interface, user_id, f'Ссылка на страницу vk.com/id{user["id"]}')
                    for photo in photos:
                        write_msg(vk_interface, user_id, attachment=f'photo{photo["owner_id"]}_{photo["media_id"]}')
                        add_data_users(user_id)
                else:
                    write_msg(vk_interface, user_id, 'внутренняя ошибка, приносим свои извинения')

            def get_photos(self, user_id, vk_interface):
                user_info = self.get_profile_info(user_id)
                info_for_search = user_validator(user_info)
                users = self.users_search(info_for_search)
                user = users.pop()
                photos = self.photos_get(user['id'])
                if photos:
                    write_msg(vk_interface, user_id,
                        f'Страница пользователя {user["first_name"]} {user["last_name"]}'
                        )
                    write_msg(vk_interface, user_id, f'Ссылка на страницу vk.com/id{user["id"]}')
                    for photo in photos:
                        write_msg(vk_interface, user_id, attachment=f'photo{photo["owner_id"]}_{photo["media_id"]}')
                        add_data_users(user_id)
                    else:
                        write_msg(vk_interface, user_id, 'внутренняя ошибка, приносим свои извинения')