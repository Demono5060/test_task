from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.profiles import *
import os
engine = create_engine("sqlite:///data.sqlite")


def database_create() -> bool:
    if not os.path.exists('data.sqlite'):
        Base.metadata.create_all(engine)
        return True
    return False


def create_profile(api_key: str, lang: str, url: str):
    with Session(engine) as session:
        profile = Profile(api_key=api_key, language=lang, url=url)
        session.add(profile)
        session.commit()


def get_first_profile() -> Profile | None:
    with Session(engine) as session:
        return session.query(Profile).first()
