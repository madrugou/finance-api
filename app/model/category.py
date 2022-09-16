from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..database.connection import Base


class Category(Base):
    __tablename__ = 'tb_category'
    __table_args__ = {'extend_existing': True, 'schema': 'madruga_db'}
    cd_category = Column(Integer, primary_key=True, autoincrement=True)
    name_category = Column(String)
    dt_created = Column(DateTime)
    dt_updated = Column(DateTime)

    def __init__(self, name):
        self.name_category = name
        self.dt_created = func.now()
        self.dt_updated = func.now()
