# -*- coding: utf-8 -*-
from db.model import Project, ProjectDatabase
from db.project import ProjectBase

__author__ = 'myth'


def test_add(project_database):
    """
      添加数据
    """

    project = ProjectBase(project_database)
    _db_session = project.db_session
    StickyNote = project.StickyNote

    sn = StickyNote()

    sn.content = u'这是一个测试内容'

    _db_session.add(sn)

    _db_session.commit()


def test_select(project_database):
    """
    查找数据
    """
    project = ProjectBase(project_database)
    # _db_session = project.db_session
    StickyNote = project.StickyNote
    sns = StickyNote.query.all()
    print sns


if __name__ == '__main__':
    project = Project.get(1)
    pd = ProjectDatabase.query.filter(ProjectDatabase.project_id == project.id).one()

    test_select(pd)
    print '='*50
    test_add(pd)
    print '='*50
    test_select(pd)