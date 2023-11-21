from sqlalchemy import Engine
from sqlalchemy.orm import Session
from models.profiles import *
import os


class Database:
    def __init__(self, engine: Engine):
        self.engine = engine

    def database_create(self) -> bool:
        if not os.path.exists('data.sqlite'):
            Base.metadata.create_all(self.engine)
            return True
        return False

    def create_profile(self, api_key: str, lang: str, url: str):
        with Session(self.engine) as session:
            profile = Profile(api_key=api_key, language=lang, url=url)
            session.add(profile)
            session.commit()

    def get_first_profile(self) -> Profile | None:
        with Session(self.engine) as session:
            return session.query(Profile).first()
