from utils.db import Database
from sqlalchemy import create_engine
from utils.settings import create_profile, get_first_profile
from utils.api import find_address
from models.profiles import Profile


def get_lat_lon(address: dict) -> tuple:
    return address.get('data').get('geo_lat'), address.get('data').get('geo_lon')


def find_needed_address(user_profile: Profile, address: str) -> dict | None:
    addresses = find_address(user_profile.url, user_profile.api_key, address)
    if addresses:
        for i in range(len(addresses)):
            print(f"{i}) {addresses[i].get('value')}")
        try:
            address_id = int(input(user_profile.get_language().choose_address))
            return addresses[address_id]
        except ValueError:
            print(user_profile.get_language().wrong_choice)
            return None


if __name__ == '__main__':
    db = Database(create_engine('sqlite:///data.sqlite'))
    if db.database_create():
        create_profile(db)
    profile = get_first_profile(db)
    while address := input(profile.get_language().get_address):
        needed_address = find_needed_address(profile, address)
        if needed_address:
            lat, lon = get_lat_lon(needed_address)
            print(f"{profile.get_language().latitude}: {lat}")
            print(f"{profile.get_language().longitude}: {lon}")
