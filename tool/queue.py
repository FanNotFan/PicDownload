#!/usr/bin/env python
# encoding: utf-8
'''
@author: lennon
@license: (C) Copyright 2019-2020, Node Supply Chain Manager Corporation Limited.
@contact: v-lefan@expedia.com
@software: pycharm
@file: Queue.py
@time: 2019-07-04 20:02
@desc:
'''
from settings import QUEUE_DEPTH

from queue import Queue

global _log_queue
_log_queue = Queue(QUEUE_DEPTH)


def log(str_log):
    _log_queue.put(str_log)


def pop():
    res = _log_queue.get()
    _log_queue.task_done()
    return res


def not_empty():
    return _log_queue.not_empty
