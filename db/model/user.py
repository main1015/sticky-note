# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from db.database import Base

__author__ = 'myth'

"""
用户类
"""


class User(Base):
    """
    用户表
    """

    __tablename__ = 'user'

    # user表自增主键
    id = Column(Integer, primary_key=True)

    #用户登录名称(唯一，通过程序控制)
    username = Column(String(80), default='', nullable=False, doc=u"用户登录名称")

    #用户邮箱(唯一，通过程序控制)
    email = Column(String(80), default='', nullable=False, doc=u"用户邮箱")

    #用户昵称(唯一，通过程序控制)
    nickname = Column(String(80), default='', nullable=False, doc=u"用户昵称")

    #用户密码
    password = Column(String(32), default='', nullable=False, doc=u"用户密码")

    # password salt
    salt = Column(String(6), default='', nullable=False, doc=u"密码加盐随机数")

    # 用户头像
    avatar = Column(String(120), default='', nullable=False, doc=u"用户头像")