# -*- coding: utf-8 -*-
from urlparse import urlparse

__author__ = 'frank'

from flask import request
from jenred import app
from jenred.util import jenkinsManager, redmineManager

@app.route('/', methods=['GET', 'POST'])
def index():
    return jenkinsManager.jenk.version

@app.route('/jenkins', methods=['GET', 'POST'])
def jenkins():
    url = request.form['url']
    job = jenkinsManager.getBuildData(url)
    app.logger.info(url)
    if job.get_status() != 'SUCCESS':
        redmineManager.postBuildResult(job)





