from tokens import com_token, user_token
from datetime import datetime

import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType

def search_profile(self, user_id):
    users = tools.users_search(info_for_search)
    user = users.pop()
    photos = tools.photos_get(user['id'])
    if photos:
        write_msg(vk_interface, user_id,
                  f'Страница пользователя {user["first_name"]} {user["last_name"]}')
        write_msg(vk_interface, user_id, f'Ссылка на страницу vk.com/id{user["id"]}')
        for photo in photos:
            write_msg(vk_interface, user_id, attachment=f'photo{photo["owner_id"]}_{photo["media_id"]}')
            add_data_users(user_id)
    else:
        write_msg(vk_interface, user_id, 'внутренняя ошибка, приносим свои извинения')

def get_photos(seif, user_id):
    user_info = tools.get_profile_info(user_id)
    info_for_search = user_validator(user_info)
    users = tools.users_search(info_for_search)
    user = users.pop()
    photos = tools.photos_get(user['id'])
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