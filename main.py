import db
import phrase
from api import Api
from phrase import *
from db import *

phrases = phrase.Ru()
dadata_url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"
api_key = ''


def create_profile():
    link = input("Ссылка для обращения к API (Нажмите Enter, если не уверены)/Api link (Press Enter if you're not "
                 "sure): ")
    if not link:
        link = dadata_url
    while True:
        api_key = input("API-ключ/API-key (https://dadata.ru/profile/#info): ")
        lang = input("Язык/Language (Ru/En): ")
        if len(api_key) != 40:
            print("Неверный API-ключ/Wrong API-key!")
        elif lang.lower() in ['ru', 'en']:
            break
    db.create_profile(api_key, lang, link)


def load_config():
    global phrases
    global api_key
    global dadata_url
    profile = db.get_first_profile()
    if profile.language == 'en':
        phrases = phrase.En
    api_key = profile.api_key
    dadata_url = profile.url


if __name__ == '__main__':
    if db.database_create():
        create_profile()
    load_config()
    api = Api(url=dadata_url, api_key=api_key)
    while address := input(phrases.get_address):
        addr = api.find_address(address)
        if addr:
            for i in range(len(addr)):
                print(f"{i}) {addr[i].get('value')}")
            try:
                id = int(input(phrases.choose_address))
                print(f"{phrases.latitude}: {addr[id].get('data').get('geo_lat')}")
                print(f"{phrases.longitude}: {addr[id].get('data').get('geo_lon')}")
            except:
                print(phrases.wrong_choice)
