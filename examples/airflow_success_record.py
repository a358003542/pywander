#!/usr/bin/env python
# -*-coding:utf-8-*-

import logging
from my_python_module.helper.airflow_helper import StatusRecordHandler


def aggregation_qidian_all_books(ds, **kwargs):
    logging.info('start process aggregation_qidian_all_books...')

    execution_date = kwargs['execution_date']
    logging.info('execution_date is {0}'.format(execution_date))

    status_handler = StatusRecordHandler(kwargs)

    task_status = status_handler.task_status
    if not task_status.get('success_book_id_list'):
        task_status['success_book_id_list'] = []

    targets = ['you', 'query', 'database']

    for target in targets:
        if target['book_id'] in task_status.get('success_book_id_list', []):
            logging.info('successful target book_id : {0}'.format(target['book_id']))
        else:

            task_status['success_book_id_list'].append(target['book_id'])
            status_handler.update_status(task_status)

    status_handler.delete()

    return 'aggregation_qidian_all_books {0} finished'.format(execution_date)
