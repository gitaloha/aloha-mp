# -*- coding: utf-8 -*-
__author__ = 'eureka'

import plogger
import traceback



def cfg_get(cfg_key):
    lines = open("config.conf", "r").readlines()
    try:
        for line in lines:
            if "#" in line:
                line = line[:line.index("#")]
            line = line.strip()
            ls = line.split("=")
            if ls[0].strip() == cfg_key:
                return ls[1].strip()
    except Exception:
        traceback.print_exc()
        return None


def init_logger():
    plogger.init_log(cfg_get("log_dir"), "aloha")

def get_logger():
    return plogger("aloha")