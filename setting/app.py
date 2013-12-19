# -*- coding: utf-8 -*-
import platform
from setting import DEV_MACHINES

__author__ = 'myth'


if platform.node() in DEV_MACHINES:
    BIND_HOST = '0.0.0.0'
    BIND_PORT = 8099
    DEBUG_ENABLED = True
else:
    BIND_HOST = '127.0.0.1'
    BIND_PORT = 8099
    DEBUG_ENABLED = False