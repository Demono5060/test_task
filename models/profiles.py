from typing import Type

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from phrase import Ru, En


class Base(DeclarativeBase):
    pass


class Profile(Base):
    __tablename__ = 'profiles'
    id: Mapped[int] = mapped_column(primary_key=True)
    api_key: Mapped[str] = mapped_column(String(40))
    language: Mapped[str] = mapped_column(String(2))
    url: Mapped[str] = mapped_column(String(1024))

    def get_language(self) -> Type[Ru | En]:
        """
        Возвращает объект, содержащий фразы
        :return: Ru | En
        """
        if self.language == 'ru':
            return Ru
        return En
