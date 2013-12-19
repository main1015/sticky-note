# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import DeclarativeMeta

__author__ = 'myth'


def set_alchemy_data(alchemy, isCover=False, **kwargs):
    """
    设置alchemy对应的值
    :param isCover: 是否覆盖已有的值
    """

    if isinstance(alchemy.__class__, DeclarativeMeta):

        # an SQLAlchemy class
        for c in alchemy.__table__.columns:
            if not c.name in kwargs:
                continue
            value = getattr(alchemy, c.name)
            if value is None or value == '':
                setattr(alchemy, c.name, kwargs.get(c.name, None))
            else:
                if isCover:
                    setattr(alchemy, c.name, kwargs.get(c.name, None))


def print_alchemy(alchemy, isForcePrint=False, print_name=[]):
    """
    打印alchemy对应的值
    :param isForcePrint: 强制打印给出的属性值,此时其他属性值不打印出来，需要配合print_name使用
    :param print_name: 需要打印的属性，需要配合isForcePrint使用
    """

    if isinstance(alchemy.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        print '<%r(' % alchemy.__class__.__name__,
        for c in alchemy.__table__.columns:
            value = getattr(alchemy, c.name)
            if isForcePrint and not c.name in print_name:
                continue

            print '%r=%r,' % (c.name, value),
        print ')>'


def repr_alchemy(alchemy):
    """
    __repr__返回的数据

    """

    repr = '<%r(' % alchemy.__class__.__name__
    columns = []
    if isinstance(alchemy.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        for c in alchemy.__table__.columns:
            value = getattr(alchemy, c.name)
            columns.append('%r=%r' % (c.name, value))
    return repr + ', '.join(columns) + ')>'