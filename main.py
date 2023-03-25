from datetime import datetime

import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
from Bot_db import *

from vk_api.exceptions import ApiError
from vk_api.utils import get_random_id

from tokens import com_token, user_token


class VkTools():
    def __init__(self, token):
        self.ext_api = vk_api.VkApi(token=token)

    def get_profile_info(self, user_id):

        try:
            info, = self.ext_api.method('users.get',
                                        {'user_id': user_id,
                                         'fields': 'bdate,city,sex,'
                                         }
                                        )
        except ApiError:
            return None
        return info

    def users_search(self, info, offset=0):

        try:
            users = self.ext_api.method('users.search',
                                        {'city_id': info['city_id'],
                                         'age_from': info['from_date'],
                                         'age_to': info['to_date'],
                                         'sex': info['sex'],
                                         'count': 50,
                                         'offset': offset
                                         }
                                        )
        except ApiError:
            return None

        try:
            users = users['items']
        except KeyError:
            return None
        result = []
        for user in users:
            if user['is_closed'] == False:
                result.append({'first_name': user['first_name'],
                               'last_name': user['last_name'],
                               'id': user['id']
                               }
                              )
        return result

    def photos_get(self, user_id):

        try:
            photos = self.ext_api.method('photos.get',
                                         {'owner_id': user_id,
                                          'album_id': 'profile',
                                          }
                                         )
        except ApiError:
            return None

        try:
            photos = photos['items']
        except KeyError:
            return None
        result = []

        for num, photo in enumerate(photos):
            result.append({'owner_id': photo['owner_id'],
                           'media_id': photo['id']
                           })
            if num == 3:
                break

            for element in photos:
                if element = ['нет фото'] and photos = 'нет фото':
                    result.append(element)
            return sorted(result)
        return result


def write_msg(interface, user_id, message=None, attachment=None):
    interface.method('messages.send',
                     {'user_id': user_id,
                      'message': message,
                      'attachment': attachment,
                      'random_id': get_random_id()}
                     )


def get_date_from_chat():
    if event.from_user:
        vk.messages.send(
            user_id=user_id,
            write_msg='Введите ваш возраст'
	        )
    pass
    return (25, 30)


def get_city_from_chat():
    if event.from_user:
        vk.messages.send(
            user_id=user_id,
            write_msg='Введите ваш город'
	        )
    pass
    return 1


def get_gender_from_chat():
    if event.from_user:
        vk.messages.send(
            user_id=user_id,
            write_msg='Введите ваш пол'
	        )
    pass
    return 1


def user_validator(info):
    result = {}
    if 'bdate' in info:
        b_year = int(info['bdate'].split('.')[2])
        now = datetime.now()
        age_uer = int(now.year) - b_year
        result['from_date'] = age_uer - 5
        result['to_date'] = age_uer + 5
    else:
        from_date, to_date = get_date_from_chat()

    if 'city' in info:
        result['city_id'] = info['city']['id']
    else:
        result['city_id'] = get_city_from_chat()

    if 'sex' in info:
        result['sex'] = 1 if info['sex'] == 2 else 2
    else:
        result['sex'] = get_gender_from_chat()

    return result


if __name__ == '__main__':
    vk_interface = vk_api.VkApi(token=com_token)
    longpoll = VkLongPoll(vk_interface)
    tools = VkTools(user_token)
    info_for_search = None
    offset = 0

    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            request = event.text.lower()
            user_id = event.user_id
            if request == 'привет':
                write_msg(vk_interface, user_id,
                          '''Привет! я бот, который поможет тебе найти свою половинку. 
                             Елси хочешь начать, пришли мне слово "поиск"'''
                          )
                user_info = tools.get_profile_info(user_id)
                if user_info:
                    info_for_search = user_validator(user_info)
                else:
                    write_msg(vk_interface, user_id,
                              '''данные не получены попробуйте позже'''
                              )

            if request == 'поиск':
                if info_for_search:
                    '''здесь дублирование'''
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


                else:
                    '''здесь дублирование'''
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

            if request == 'дальше':
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

                if len(users) == 0:
                    users = tools.users_search(info_for_search, offset=offset + 50)

            elif request == "пока":
                write_msg(vk_interface, event.user_id, "Пока((")
            else:
                write_msg(vk_interface, user_id, "Не поняла вашего ответа...")