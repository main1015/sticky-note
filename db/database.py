# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db import Base, _Base

__author__ = 'myth'


engine = create_engine('sqlite:////tmp/sticky-note.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
# Base = declarative_base()
Base.query = db_session.query_property()


def get_db_base(db_name):

    db_base = declarative_base(cls=_Base)

    db_engine = create_engine('sqlite:////tmp/%s' % db_name, convert_unicode=True)
    session = scoped_session(sessionmaker(autocommit=False,
                                          autoflush=False,
                                          bind=db_engine))
    db_base.query = session.query_property()

    return db_base, session, db_engine


def init_db():
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    import model
    Base.metadata.create_all(bind=engine)