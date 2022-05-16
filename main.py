import requests
import json


def get_token():
    url1 = "https://**********/Token/get"
    content = {'appId':'***','appSecret':'******'}
    web = requests.get(url=url1,params=content)
    print(web.url)
    print(web.text)
    ty = web.text
    a = json.loads(ty)
    b = a.get('Data')
    apptoken = b.get('Token')
    return apptoken


if __name__ == '__main__':
    get_token()
