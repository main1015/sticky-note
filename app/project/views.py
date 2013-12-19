# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

__author__ = 'myth'

project_page = Blueprint('project_page', __name__)


@project_page.route("/project/<string:name>")
def project(name):
    """
    项目主页
    """

    return render_template("/d_and_d.html")
