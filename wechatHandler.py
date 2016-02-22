# -*- coding: utf-8 -*-
__author__ = 'eureka'

import tornado.web
import traceback
import logging

from config import *

from wechat_sdk import WechatConf,WechatBasic

logger = logging.getLogger("root")

class BaseWechatHandler(tornado.web.RequestHandler):
    def initialize(self):
        conf = WechatConf(
            token = cfg_get("token"),
            appid= cfg_get("appid"),
            token = cfg_get("token"),
            encrypt_mode = cfg_get("encrypt_mode"),
            encoding_aes_key = cfg_get("encoding_aes_key")
        )
        self._wechat = WechatBasic(conf=conf)
        init_logger()


class RootHandler(BaseWechatHandler):
    def get(self, *args, **kwargs):
        if self._wechat.check_signature(self.get_argument("signature"), self.get_argument("signature"), self.get_argument("signature")):
            logger.debug("accept")
        else:
            logger.debug('Wrong')

