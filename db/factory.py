# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import DeclarativeMeta
from db.database import get_db_base

__author__ = 'myth'

"""
数据库模型工厂
"""


class FactoryException(TypeError):
    pass


def factory_alchemy(alchemy, base, session, engine):
    """
    :param alchemy: class
    """

    if issubclass(alchemy.__class__, DeclarativeMeta):
        Alchemy = type(alchemy.__name__, (alchemy, base), {"query": session.query_property()})

        return Alchemy
    else:
        raise FactoryException("'%s' class is not DeclarativeMeta" % alchemy.__name__)



def factory_init_db(project_database, alchemies):
    """
    :param alchemies: 里面的类名不能重复，使用as也不行
    """
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    base, session, engine = get_db_base(db_name=project_database.db_name)
    _alchemies = []
    if not isinstance(alchemies, list):
        _alchemies.append(alchemies)
    else:
        _alchemies.extend(alchemies)
    tables = []
    for alchemy in _alchemies:
        Alchemy = factory_alchemy(alchemy, base, session, engine)
        # globals()[Alchemy.__name__] = Alchemy
        tables.append(Alchemy.__table__)
    base.metadata.create_all(bind=engine, tables=tables)