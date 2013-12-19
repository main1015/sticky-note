# -*- coding: utf-8 -*-
import platform
from setting import DEV_MACHINES, STAG_MACHINES, PRO_MACHINES

__author__ = 'myth'

"""
数据库配置文件
"""

DB_CHARSET = 'utf8'

if platform.node() in DEV_MACHINES:
    pass
elif platform.node() in STAG_MACHINES:
    pass
elif platform.node() in PRO_MACHINES:
    pass
else:
    pass