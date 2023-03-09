import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from Bot_db import UserStatus, user_list, update_status, check_or_create_user, search_users, get_photo
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

searching = search_users(sex, age, city)

            searching = search_users(sex, age, city)

            for i in range(len(searching)):
                dating_user = check_or_create_user(searching[i][3])
                user_photo = get_photo(searching[i][3])
                if  dating_user == None:
                    user(searching[i][0], searching[i][1], searching[i][2], searching[i][3])
                    link = searching[i][3]
                    write_msg_with_att(user_id, photo, link)
                    write_msg(user_id, 'Продолжаем поиск? - y\n'
                                        'Закончить поиск / Выход - n')
                    request, user_id = reboot_bot()
                    if request == '1':
                        continue
                    elif request == '2':
                        write_msg(user_id, 'Нажми любую кнопку для перезапуска')
                        break
                    else:
                        write_msg(user_id, 'Нажми что угодно!')
                        break
                else:
                    continue
            write_msg(user_id, 'Нажми что угодно!')