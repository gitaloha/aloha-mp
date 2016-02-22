# -*- coding: utf-8 -*-
__author__ = 'eureka'

import tornado.web
import traceback
import logging

import config 

from wechat_sdk import WechatConf,WechatBasic

logger = logging.getLogger("root")

class BaseWechatHandler(tornado.web.RequestHandler):
    def initialize(self):
        conf = WechatConf(
            token = config.cfg_get("token"),
            appid=config.cfg_get("appid"),
            appsecret = config.cfg_get("appsecret"),
            encrypt_mode = config.cfg_get("encrypt_mode"),
            encoding_aes_key = config.cfg_get("encoding_aes_key")
        )
	
        self._wechat = WechatBasic(conf=conf)
        config.init_logger()


class RootHandler(BaseWechatHandler):
    def get(self, *args, **kwargs):
	print self.get_argument("signature"), self.get_argument("timestamp"), self.get_argument("nonce")
        if self._wechat.check_signature(self.get_argument("signature"), self.get_argument("timestamp"), self.get_argument("nonce")):
            logger.debug("accept")
	    print "accept"
	    self.write(self.get_argument('echostr'))
        else:
            logger.debug('Wrong')
	    print "wrong"

