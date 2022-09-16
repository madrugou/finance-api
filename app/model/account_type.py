from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..database.connection import Base


class AccountType(Base):
    __tablename__ = 'tb_account_type'
    __table_args__ = {'extend_existing': True, 'schema': 'madruga_db'}
    cd_type = Column(Integer, primary_key=True, autoincrement=True)
    name_type = Column(String)
    dt_created = Column(DateTime)
    dt_updated = Column(DateTime)

    def __init__(self, name):
        self.name_type = name
        self.dt_created = func.now()
        self.dt_updated = func.now()
