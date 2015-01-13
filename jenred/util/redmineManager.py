# -*- coding: utf-8 -*-
__author__ = 'frank'
from jenkinsapi import build
from jenred import config,app
from datetime import date
from redmine import Redmine


def postBuildResult(buildResult):
    try:
        issue = _createIssue(buildResult)
        red = Redmine(config.REDMINE_SERVER, username=config.REDMINE_USERNAME, password=config.REDMINE_PWD)
        issue.post(red)
    except Exception as e:
        print e
        app.logger.exception(e)

def _createIssue(buildResult):
    subject = _genSubject(buildResult)
    description = buildResult.get_result_url()
    jobName = buildResult.job.name
    return Issue(config.JENKINS_PROJECT_DIC[jobName],subject,description)

def _genSubject(buildResult):
    return  config.REDMINE_SUBJECT_PRE+str(buildResult)\
            +' '+str(buildResult.get_status())

class Issue(object):
    def __init__(self,project,subject,description='',
                tracker_id=1,start_date=date.today()):
        self.subject = subject
        self.project = project
        self.description = description
        self.tracker_id = tracker_id
        self.start_date = start_date

    def post(self,redmine):
        redmine.issue.create(project_id=self.project,
                             subject=self.subject,
                             tracker_id=self.tracker_id,
                             description=self.description,
                             start_date=self.start_date)