# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, SMALLINT, Enum
from db.database import Base

__author__ = 'myth'

"""
项目类
"""


class Project(Base):
    """
    项目类
    """
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)

    #项目名称
    name = Column(String(32), default='', nullable=False, doc=u"项目名称")

    #项目web路径
    path = Column(String(32), default='', nullable=False, doc=u"项目web路径")


class ProjectDatabase(Base):
    """
    项目数据库类
    """
    __tablename__ = 'project_database'

    id = Column(Integer, primary_key=True)

    #project 表id
    project_id = Column(Integer, default=0, nullable=False, doc=u'project 表id')

    #数据库的名称
    db_name = Column(String(32), default='', nullable=False, doc=u'数据库的名称')

    #数据库类型,见DatabasesType类
    db_type = Column(SMALLINT, default=0, nullable=False, doc=u'数据库类型')

    #数据库的用户名
    db_user = Column(String(32), default='', nullable=False, doc=u'数据库的用户名')

    #数据库的密码
    db_password = Column(String(32), default='', nullable=False, doc=u'数据库的密码')

    #数据库地址
    db_host = Column(String(32), default='', nullable=False, doc=u'数据库地址')

    #数据库端口
    db_port = Column(String(32), default='', nullable=False, doc=u'数据库端口')


class DatabaseType(Enum):

    #sqlite
    SQLITE = 1

    #mysql
    MYSQL = 2