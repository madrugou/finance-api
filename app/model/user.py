from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..database.connection import Base


class User(Base):
    __tablename__ = 'tb_user'
    __table_args__ = {'extend_existing': True, 'schema': 'madruga_db'}
    cd_user = Column(Integer, primary_key=True, autoincrement=True)
    name_user = Column(String)
    email_user = Column(String)
    password = Column(String)
    dt_created = Column(DateTime)
    dt_updated = Column(DateTime)

    def __init__(self, name, email, password):
        self.name_user = name
        self.email_user = email
        self.password = password
        self.dt_created = func.now()
        self.dt_updated = func.now()

    def __repr__(self):
        return f"<User>: {self.name_user}"
