import re


def is_correct_link(link: str) -> bool:
    """
    Проверяет корретность ссылки используя регулярное выражение
    находит ссылки формата
    http://regex101.com/
    https://regex101.com/etc?1=1
    www.regex101.com/etc/etc
    :param link: ссылка
    :return:
    """
    pattern = r"^((http|https):\/\/)?(www\.)?([A-Za-zА-Яа-я0-9]{1}" \
              r"[A-Za-zА-Яа-я0-9\-]*\.?)*\.{1}[A-Za-zА-Яа-я0-9-]{2," \
              r"8}(([\w#!:.?+=&%@!\-\/])*)?"
    if re.search(pattern, link):
        return True
    return False


def is_correct_api_key(api_key: str) -> bool:
    """
    Проверяет корректность ключа (сейчас проверяет ТОЛЬКО длину)
    :param api_key: апи-ключ
    :return:
    """
    if len(api_key) == 40:
        return True
    return False


def is_correct_lang(lang: str) -> bool:
    """
    Проверяет корректность выбранного языка
    :param lang: язык
    :return:
    """
    if lang.lower() in ['ru', 'en']:
        return True
    return False


def input_link() -> str:
    """
    Запрашивает ссылку у пользователя и возвращает, если пользователь ввел её
    :return: ссылка
    """
    link = ''
    while not is_correct_link(link):
        link = input("Ссылка для обращения к API (Нажмите Enter, если не уверены)/"
                     "Api link (Press Enter if you're not "
                     "sure): ")
        if not link:
            link = "https://suggestions.dadata.ru/suggestions/" \
                   "api/4_1/rs/suggest/address"
    return link


def input_api_key() -> str:
    """
    запрашивает апи-ключ пользователя
    :return: апи-ключ
    """
    api_key = ''
    while not is_correct_api_key(api_key):
        api_key = input("API-ключ/API-key (https://dadata.ru/profile/#info): ")
    return api_key


def input_lang() -> str:
    """
    запрашивает язык пользователя
    :return: язык
    """
    lang = ''
    while not is_correct_lang(lang):
        lang = input("Язык/Language (Ru/En): ")
    return lang
