#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
bundle = Blueprint('home', __name__, template_folder='templates')


@bundle.route('/', methods=['GET', 'POST'])
def index():
    try:
        return render_template('home/index.html')
    except TemplateNotFound:
        abort(404)
