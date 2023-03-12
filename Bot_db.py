import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from tokens import token, user_token


user_list = {}


class UserStatus(Enum):
    IDLE = 'idle'
    DATA_UPDATING = 'data_updating'


def check_or_create_user(self, user_id):
    if user_id in user_list:
        return True
    user = {
        'data': {
            'age': {},
            'sex': {},
            'city': {},
        },
        'status': UserStatus.IDLE.value
    }
    user_list.update({user_id: user})
    return False

def update_status(user_id, status):
    user = user_list.get(user_id)

    user['status'] = status.value
    user_list.update({user_id: user})
