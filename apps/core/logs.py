#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    :   2023/11/05 21:10:34
@Author  :   yuqibing 
@Desc    :   
'''
import logging
import re
import os

from logging.handlers import TimedRotatingFileHandler

service_log = logging.getLogger("service_log")

LOG_FORMAT = '''
{\"ts\": \"%(asctime)s\", 
 \"log_type\": \"service\", \"message\":%(message)s}'''.replace('\n', '').strip()


dir_name = './../logs'
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

file_path = os.path.join(dir_name, 'mylog')

file_handler = TimedRotatingFileHandler(
        filename=file_path, when="MIDNIGHT", interval=1, backupCount=60
    )
# filename="mylog" suffix设置，会生成文件名为mylog.2023-09-25.log
file_handler.suffix = "%Y-%m-%d.log"

# 需要注意的是suffix和extMatch一定要匹配的上，如果不匹配，过期日志不会被删除。
file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")


stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_formatter = logging.Formatter(LOG_FORMAT)
stream_handler.setFormatter(stream_formatter)
service_log.addHandler(stream_handler)

formatter = logging.Formatter(LOG_FORMAT, datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)

service_log.setLevel(logging.INFO)
service_log.addHandler(file_handler)
