# -*- coding: utf-8 -*-
__author__ = 'frank'

from flask import request
from jenred import app

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'index'

@app.route('/jenkins', methods=['GET', 'POST'])
def jenkins():
    data = request.form['url']
    app.logger.info(data)



