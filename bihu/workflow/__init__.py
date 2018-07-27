#!/usr/bin/env python
# -*-coding:utf-8-*-

"""

本模块主要放着和工作流程管理相关的函数

"""
from bihu.database.sqldb.workflow_models import RunningTaskProgress, session as session_workflow


def get_airflow_unique_string(kwargs):
    task_instance = kwargs['task_instance']
    run_id = kwargs['run_id']

    unique_string = '{0}_{1}_{2}'.format(task_instance.dag_id, task_instance.task_id, run_id)
    return unique_string


class StatusRecordHandler(object):
    def __init__(self, kwargs):
        self.airflow_unique_string = get_airflow_unique_string(kwargs)
        self.status_record = session_workflow.query(RunningTaskProgress).filter_by(
            airflow_unique_string=self.airflow_unique_string).first()

        if self.status_record:
            self.task_status = self.status_record.status
        else:
            self.status_record = RunningTaskProgress(airflow_unique_string=self.airflow_unique_string, status={})
            session_workflow.add(self.status_record)
            session_workflow.commit()
            self.task_status = self.status_record.status

    def delete(self):
        session_workflow.delete(self.status_record)
        session_workflow.commit()

    def update_status(self, status):
        self.status_record.status = status
        session_workflow.commit()
