# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from db import status_mixin, timestamp_mixin
from db.database import Base

__author__ = 'myth'


@status_mixin
@timestamp_mixin
class Task(Base):
    """
    项目任务表
    """
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)

    #任务表所在的项目（project）表id
    project_id = Column(Integer, default=0, nullable=False, doc=u'任务表所在的项目（project）表id')

    #任务名称
    name = Column(String(32), default='', nullable=False, doc=u"任务名称")


@status_mixin
@timestamp_mixin
class TaskStep(Base):
    """
    任务步骤表
    """

    __tablename__ = 'task_step'

    id = Column(Integer, primary_key=True)

    #步骤表所在的任务（task）表id
    task_id = Column(Integer, default=0, nullable=False, doc=u'步骤表所在的任务（task）表id')

    #步骤名称
    name = Column(String(32), default='', nullable=False, doc=u"步骤名称")

    #步骤的次序
    rank = Column(Integer, default=1, nullable=False, doc=u'步骤的次序')