# -*- coding: utf-8 -*-
from db.database import get_db_base
from db.factory import factory_alchemy
from db.model.note import StickyNote, NotePosition

__author__ = 'myth'


class ProjectBase(object):
    """
    返回项目相关的数据库模型
    """
    def __init__(self, project_database):

        base, session, engine = get_db_base(db_name=project_database.db_name)

        self.Base = base
        self.db_session = session
        self.engine = engine

    @property
    def StickyNote(self):
        """
        StickyNote模型
        """
        Alchemy = factory_alchemy(StickyNote, self.Base, self.db_session, self.engine)
        return Alchemy

    @property
    def NotePosition(self):
        """
        NotePosition模型
        """
        Alchemy = factory_alchemy(NotePosition, self.Base, self.db_session, self.engine)
        return Alchemy