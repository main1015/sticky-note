# -*- coding: utf-8 -*-
import os
from flask import Flask, send_from_directory
from werkzeug.contrib.fixers import ProxyFix
from setting.app import DEBUG_ENABLED
from app.project.views import project_page
from app.task.views import task_page

__author__ = 'myth'


# Application config.
app = Flask(__name__, template_folder="../templates")
app.debug = DEBUG_ENABLED
app.wsgi_app = ProxyFix(app.wsgi_app)


app.register_blueprint(project_page)
app.register_blueprint(task_page)


@app.route('/favicon.ico')
def favicon():
    """
    favicon.ico
    """

    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')