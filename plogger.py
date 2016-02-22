# -*- coding: utf-8 -*-
__author__ = 'eureka'

import os, os.path
import time
import logging


def init_log(log_dir, name):
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)
    if log_dir[-1] != os.sep:
        log_dir+= os.sep
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    today = log_dir + time.strftime("%Y-%m-%d", time.localtime()) + ".log"
    fh = logging.FileHandler(today)
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)

def get_logger(name):
    return logging.getLogger(name)