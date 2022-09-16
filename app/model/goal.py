from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Float
from ..database.connection import Base
from sqlalchemy.sql import func


class Goal(Base):
    __tablename__ = 'tb_goal'
    __table_args__ = {'extend_existing': True, 'schema': 'madruga_db'}
    cd_goal = Column(Integer, primary_key=True, autoincrement=True)
    name_goal = Column(String)
    balance_initial = Column(Float)
    balance_final = Column(Float)
    dt_initial = Column(Date)
    dt_final = Column(Date)
    cd_user = Column(Integer, ForeignKey('madruga_db.tb_user.cd_user'))
    dt_created = Column(DateTime)
    dt_updated = Column(DateTime)

    def __init__(self, name, value_initial, value_final, dt_initial, dt_final):
        self.name_goal = name
        self.balance_initial = value_initial
        self.balance_final = value_final
        self.dt_initial = dt_initial
        self.dt_final = dt_final
        self.dt_created = func.now()
        self.dt_updated = func.now()
