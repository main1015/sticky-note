# -*- coding: utf-8 -*-
from app import app
from setting.app import BIND_HOST, BIND_PORT, DEBUG_ENABLED

__author__ = 'myth'


if __name__ == '__main__':
    app.run(host=BIND_HOST, port=BIND_PORT, debug=DEBUG_ENABLED)