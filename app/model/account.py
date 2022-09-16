from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from ..database.connection import Base
from sqlalchemy.sql import func


class Account(Base):
    __tablename__ = 'tb_account'
    __table_args__ = {'extend_existing': True, 'schema': 'madruga_db'}
    cd_account = Column(Integer, primary_key=True, autoincrement=True)
    name_account = Column(String)
    balance = Column(Float)
    cd_user = Column(Integer, ForeignKey("madruga_db.tb_user.cd_user")) # User user.cd_user
    cd_type = Column(Integer, ForeignKey("madruga_db.tb_account_type.cd_type"))
    dt_created = Column(DateTime)
    dt_updated = Column(DateTime)

    def __init__(self, name_account, balance, cd_user, cd_type):
        self.name_account = name_account
        self.balance = balance
        self.cd_user = cd_user
        self.cd_type = cd_type
        self.dt_created = func.now()
        self.dt_updated = func.now()
