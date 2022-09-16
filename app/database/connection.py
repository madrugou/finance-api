from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..environment import configuration

engine = create_engine(configuration['POSTGRE_URL'])
Session = sessionmaker(bind=engine)
Base = declarative_base()

