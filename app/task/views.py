# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

__author__ = 'myth'


task_page = Blueprint('task_page', __name__)


@task_page.route("/task/<string:name>")
def task(name):
    """
    任务主页
    """

    return render_template("/task/index.html")
