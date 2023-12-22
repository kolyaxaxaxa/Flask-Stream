import json

from config import vk_token
import requests

TOKEN = vk_token
session = requests.Session()

class getUsersInfo():
    r = session.get('https://api.vk.com/method/users.get', params={
        'access_token': vk_token,
        'v': 5.154,
        'lang': 0,
        'user_ids': 155323128,
        'fields': 'bdate, city'
    })

    dataGetUsersInfo = r.json()
    with open('UsersInfo.json', 'w', encoding='utf8') as file:
        json.dump(dataGetUsersInfo, file, indent=2, ensure_ascii=False)

    # first_name = dataGetUsersInfo['response'][0]['first_name']
    # last_name = dataGetUsersInfo['response'][0]['last_name']
    # bdate = dataGetUsersInfo['response'][0]['bdate']
    # city = dataGetUsersInfo['response'][0]['city']['title']
    # bdate = dataGetUsersInfo.get('bdate', '')
    # city = dataGetUsersInfo.get('city', '')

    # print(f'Имя пользователя {first_name} {last_name}')



