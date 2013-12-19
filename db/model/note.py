# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Text, Float, String, SMALLINT
from db.database import Base
from db import status_mixin, timestamp_mixin

__author__ = 'myth'
"""
便利贴model
"""


@status_mixin
@timestamp_mixin
class StickyNote(Base):
    """
    便签基础类
    """

    __tablename__ = 'sticky_note'
    id = Column(Integer, primary_key=True)

    #便签所在的项目（project）表id
    project_id = Column(Integer, default=0, nullable=False, doc=u'便签所在的项目（project）表id')

    #便签所在的任务（task）表id
    task_id = Column(Integer, default=0, nullable=False, doc=u'便签所在的任务（task）表id')

    #便签所在的步骤（task_step）表id
    step_id = Column(Integer, default=0, nullable=False, doc=u'便签所在的步骤（task_step）表id')

    # 便签标题
    subject = Column(String(32), default='', nullable=False, doc=u"便签标题")

    # 便签内容
    content = Column(Text, default='', nullable=False, doc=u"便签内容")


@timestamp_mixin
class NoteProperty(Base):
    """
    便签属性类
    """
    __tablename__ = 'note_property'

    id = Column(Integer, primary_key=True)

    #sticky_note 表id
    note_id = Column(Integer, default=0, nullable=False, doc=u'sticky_note 表id')

    #背景色
    background_color = Column(String(32), default='', nullable=False, doc=u'背景色')

    #便签的状态
    status = Column(SMALLINT, default=0, nullable=False, doc=u"便签的状态")


@timestamp_mixin
class NotePosition(Base):
    """
    便签位置类
    """

    __tablename__ = 'note_position'

    id = Column(Integer, primary_key=True)

    #sticky_note 表id
    note_id = Column(Integer, default=0, nullable=False, doc=u'sticky_note 表id')

    #便签在web页面上的x坐标
    x = Column(Float, default=0.0, nullable=False, doc=u'便签在web页面上的x坐标')

    #便签在web页面上的y坐标
    y = Column(Float, default=0.0, nullable=False, doc=u'便签在web页面上的y坐标')

    #便签在web页面上的z坐标
    z = Column(Float, default=0.0, nullable=False, doc=u'便签在web页面上的z坐标')


# @timestamp_mixin
# class NotePositionHistory(Base):
#     """
#     便签位置历史记录表
#     """
#
#     __tablename__ = 'note_position_history'
#
#     id = Column(Integer, primary_key=True)
#
#     #sticky_note 表id
#     note_id = Column(Integer, default=0, nullable=False, doc=u'sticky_note 表id')
#
#     #便签在web页面上的x坐标
#     x = Column(Float, default=0.0, nullable=False, doc=u'便签在web页面上的x坐标')
#
#     #便签在web页面上的y坐标
#     y = Column(Float, default=0.0, nullable=False, doc=u'便签在web页面上的y坐标')
#
#     #便签在web页面上的z坐标
#     z = Column(Float, default=0.0, nullable=False, doc=u'便签在web页面上的z坐标')
#
#     #便签上次任务所在的位置id，与历史记录表关联
#     # history_id = Column(Integer, default=0, nullable=False, doc=u'便签上次任务所在的位置id')