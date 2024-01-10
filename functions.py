import requests
from settings import settings as setting
from api_routes import routes as route


base_url = setting.api_base_url
init_chat_route = route.chat_init
get_all_chats_route = base_url + route.chat_get_all

header = {
    'accept': 'application/json',
    'Authorization': ''}

def init_chat(token):
    header['Authorization'] = 'Bearer ' + token
    response = requests.post(init_chat_route, headers=header)
    return response.json()


def get_all_chats(token):
    header['Authorization'] = 'Bearer ' + token
    response = requests.get(get_all_chats_route, headers=header)
    return response.json()