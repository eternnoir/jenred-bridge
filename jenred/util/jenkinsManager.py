# -*- coding: utf-8 -*-
from urlparse import urlparse
from types import IntType

__author__ = 'frank'
from jenred import config, app
from jenkinsapi.jenkins import Jenkins

def getBuildData(url):
    job= None
    try:
        pars = urlparse(url)
        portco = pars.scheme
        host = pars.netloc
        paths = str(pars.path).split('/')
        jobName = paths[2]
        buildId = paths[3]
        job = _getBuildData(jobName,int(buildId),portco+'://'+host)
    except Exception as e:
        app.logger.exception(e)
    return job


def _getBuildData(jobId,buildNum,host=config.JENKINS_SERVER):
    j = Jenkins(host,config.JENKINS_USERNAME,config.JENKINS_PWD)
    assert type(buildNum) is IntType, "id is not an integer: %r" % id
    buildData = j.get_job(jobId).get_build(buildNum)
    app.logger.info("GET "+jobId+" "+str(buildNum))
    return buildData
