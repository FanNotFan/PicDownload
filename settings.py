#!/usr/bin/env python
# encoding: utf-8
'''
@author: lennon
@license: (C) Copyright 2019-2020, Node Supply Chain Manager Corporation Limited.
@contact: v-lefan@expedia.com
@software: pycharm
@file: settings.py.py
@time: 2019-06-25 15:52
@desc:
'''

import os
import platform
from multiprocessing import cpu_count
# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

# get system info
PLATFORM_SYSTEM = platform.system()
print("PLATFORM_SYSTEM: {}".format(PLATFORM_SYSTEM))

# Webdriver server url
WEBDRIVER_SERVER_URL = "http://10.184.144.20:4444/wd/hub"

# 网页打开后停留时间，单位是秒(Seconds)
WAIT_WEBSITE_DELAY_TIME = 3

# 存储消息队列的长度
QUEUE_DEPTH = 10

# Whether to open multiple processes
WHETHER_OPEN_MULTIPLE_PROCESSES = True

# Number of processes opened 开启的进程数
NUMBER_OF_PROCESSES = cpu_count()

VERSION = 'v5.8.2-ML-Beta'