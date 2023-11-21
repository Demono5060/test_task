from models.profiles import Profile
from utils.input_utils import input_link, input_lang, input_api_key


def create_profile(database) -> None:
    """
    Создает профиль и сохраняет его в базу данных
    :param database: база данных
    :return:
    """
    link = input_link()
    key = input_api_key()
    lang = input_lang()
    database.create_profile(key, lang, link)


def get_first_profile(database) -> Profile | None:
    """
    Возвращает первый профиль в базе данных
    :param database: база данных
    :return: профиль
    """
    return database.get_first_profile()
