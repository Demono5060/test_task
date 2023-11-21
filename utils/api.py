import requests
import json


def find_address(url: str, api_key: str, address: str) -> dict | None:
    """
    подставляет address в json параметры, добавляет хэдеры и делает запрос
    возвращает адреса, если ответ от сервера соответствует ожидаемому
    :param url: ссылка для запроса
    :param api_key: ключ
    :param address: адрес
    :return: результат запроса
    """
    headers = {'Authorization': 'Token ' + api_key,
               'Content-Type': 'application/json',
               'Accept': 'application/json'}
    json_params = {'query': address}
    r = requests.post(url, json=json_params, headers=headers)
    if r.status_code == 200:
        return json.loads(r.text).get('suggestions')
    elif r.status_code == 403:
        raise 'Wrong api-key'
