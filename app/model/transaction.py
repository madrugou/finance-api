from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Float
from ..database.connection import Base
from sqlalchemy.sql import func


class Transaction(Base):
    __table_name__ = "tb_transaction"
    __table_args__ = {"extend_existing": True, "schema": "madruga_db"}
    cd_transaction = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    value = Column(Float)
    cd_user = Column(Integer, ForeignKey("madruga_db.tb_user.cd_user"))
    cd_category = Column(Integer, ForeignKey("madruga_db.tb_category.cd_category"))
    dt_transaction = Column(Date)
    dt_created = Column(DateTime)
    dt_updated = Column(DateTime)

    def __init__(self, description, value, dt_transaction):
        self.description = description
        self.value = value
        self.dt_transaction = dt_transaction
        self.dt_created = func.now()
        self.dt_updated = func.now()
