from sqlalchemy import Column, Integer, String

from database import Base


class Game(Base):
    __tablename__ = "Games"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(String, nullable=False)
    cover_url = Column(String, nullable=False)
    description = Column(String, nullable=False)
    publisher = Column(String, nullable=True)
    release_date = Column(String, nullable=True)