# -*- coding: utf-8 -*-
from db.database import db_session
from db.model import Project, ProjectDatabase
from db.model.project import DatabaseType

__author__ = 'myth'
"""
数据库初始化
"""


def init_project():
    project = Project()
    project.name = u'我的第一个项目'
    db_session.add(project)
    db_session.commit()

    project_database = ProjectDatabase()
    project_database.project_id = project.id
    project_database.db_name = 'first.db'
    project_database.db_type = DatabaseType.SQLITE
    db_session.add(project_database)
    db_session.commit()


if __name__ == '__main__':
    init_project()