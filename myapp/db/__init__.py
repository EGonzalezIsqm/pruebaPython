from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import scoped_session, mapper
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('mysql://python:prueba12345@localhost/dbpython', convert_unicode=True)
metadata = MetaData(bind=engine)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


class Model(object):
    query = session.query_property()
