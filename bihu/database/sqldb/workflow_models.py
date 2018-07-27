#!/usr/bin/env python
# -*-coding:utf-8-*-


"""

工作流那边额外建立的一些数据库

"""


from dynaconf import settings
from datetime import datetime

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from .conn import sqldb_workflow_url

engine = create_engine(sqldb_workflow_url)
metadata = MetaData(bind=engine)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()



class RunningTaskProgress(Base):
    """
    airflow 正在运行的任务 进度记录，已经运行完了记录将会被删除

    airflow那边正在运行的任务唯一性标识 {dag_id}_{task_id}_{running_id}

    每个任务启动时建立这样一条记录，内部有任务进度计数，积极捕捉异常，异常发生后，

    status 字段里面根据需要保存一些必要的信息，后面的任务运行根据这些必要的信息来决定跳过某些任务处理步骤


    每个任务正常跑完之后，删除本记录
    每个任务启动前，检查时候有目标记录，如果有，则根据 记录跳过一些运算任务。
    """
    __tablename__ = 'running_task_progress'

    id = Column(Integer, primary_key=True)

    airflow_unique_string = Column(String(511), unique=True, nullable=False)

    status = Column(JSON)