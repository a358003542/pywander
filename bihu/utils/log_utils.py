#!/usr/bin/env python
# -*-coding:utf-8-*-



from fluent import sender
import time
import logging

class FluentdLogger(object):
    def __init__(self, project_name = 'bihu', host='localhost', port=24224, nanosecond_precision=True):
        self._logger = sender.FluentSender('fluentd.{0}'.format(project_name), host=host,
                                           port=port, nanosecond_precision=nanosecond_precision)


    def send(self, domain, msg, curtime=None):
        curtime = time.time() if curtime is None else curtime # 实际发送的时间，若后面有错误，仍然以这个时间为准

        # msg add source
        msg['source'] = domain

        # 重复发三次，如果还是失败，那么只好打印出来了
        count = 0
        while not self.logger.emit_with_time(domain, curtime, msg):
            print(self.logger.last_error)
            logging.error(self.logger.last_error)

            self.logger.clear_last_error()

            count += 1

            if count >= 3:
                break


    @property
    def logger(self):
        return self._logger

    def close(self):
        self.logger.close()


def create_mongodb_op_log(query_id, op_type, op_targets):
    msg = {
        'query_id': query_id,
        'op_type': op_type,
        'op_targets': op_targets
    }
    return msg


