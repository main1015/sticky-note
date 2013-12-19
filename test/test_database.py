# -*- coding: utf-8 -*-
import inspect
from db.database import get_db_base
from db.factory import factory_alchemy, factory_init_db
from db.model.note import StickyNote, NotePosition
from db.model import Project, ProjectDatabase

__author__ = 'myth'


def test_print_db_repr(alchemy):
    """
    测试数据库模型类的打印方法
    """
    print alchemy


def test_db_factory_alchemy(alchemy):
    base, session, engine = get_db_base(db_name='project')
    Alchemy = factory_alchemy(alchemy, base, session, engine)
    print inspect.getmro(Alchemy)
    print Alchemy()


def test_db_factory_init_db(project_database, alchemy):

    factory_init_db(project_database, alchemy)


if __name__ == '__main__':

    project = Project.get(1)
    test_print_db_repr(project)

    test_db_factory_alchemy(StickyNote)
    pd = ProjectDatabase.query.filter(ProjectDatabase.project_id == project.id).first()
    print pd
    pd = ProjectDatabase.query.filter(ProjectDatabase.project_id == project.id).one()
    test_db_factory_init_db(pd, [StickyNote, NotePosition])
