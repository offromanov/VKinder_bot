import vk_api
import requests
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from Bot_db import UserStatus, user_list, update_status, check_or_create_user
from tokens import token, user_token

vk = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(bh, group_id='219207094')

if __name__='__main__':
    while True:
        if request, user_id = reboot_bot()

def write_msg(user_id, additional):
    message_payload = {'peer_id': user_id, 'random_id': 0, **additional}
    vk.method('messages.send', message_payload)

for event in longpoll.listen():

    if event.type == VkBotEventType.MESSAGE_NEW:
        request = event.object.message['text'].lower()
        user_id = event.object.message['from_id']
        if not check_or_create_user(user_id):
            write_msg(user_id, {'message': 'Привет! я бот, который поможет тебе найти свою половинку. Елси хочешь '
                'начать, пришли мне слово "Данные"',)

        elif request == 'данные':
            update_status(user_id, UserStatus.DATA_UPDATING)
            write_msg(user_id, {'message': ''''Давай заполним твои данные: 
                                Пришли свои данные в формате:
                                Пол - мужской или женский;
                                Город - (Например: Санкт-Петербург);
                                Возраст - (Например: 22)'''})


        elif request == "пока":
                write_msg(event.user_id, "Пока((")
    else:
        write_msg(event.user_id, "Не поняла вашего ответа...")

def search_user(user_id):
    request_paramas = {
                'access_token': user_token,
                'v': '5.131',
                'age': self.check_or_create_user(user_id),
                'sex': self.check_or_create_user(user_id),
                'city': self.check_or_create_user(user_id),}

    if request_paramas:
        if request_paramas.get('items'):
            return request_paramas.get('items')
        write_msg(user_id, 'Ошибка')
        return False

def search_foto(user_id):
    try:
        request_params = {
            'access_token': user_token,
            'v': '5.131',
            'albumn_id': 'profile',
            'extended': '1'}
        if request_paramas.get('count'):
            if request_paramas.get('count') < 3:
                return False
            top_photos = sorted(request_paramas.get('items'), key=lambda x: x['likes']['count']
                                + x['comments']['count'], reverse=True)[:3]
            photo_data = {'user_id': top_photos[0]['access_token'], 'photo_ids': []}
            for photo in top_photos:
                photo_data['photo_ids'].append(photo['id'])
            return photo_data
        return False
    except vk_api.exceptions.ApiError as error:
        print(error)