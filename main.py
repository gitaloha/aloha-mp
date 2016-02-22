# -*- coding: utf-8 -*-
__author__ = 'eureka'

import os, os.path

import tornado.ioloop
import tornado.web

from wechatHandler import  *

def make_app():
    setting = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret": "61oETzKXQAalsdfgYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        "xsrf_cookies": True,
        "debug": True,
        "template_path": "template"
    }
    application = tornado.web.Application([
        (r"/mp", RootHandler),
    ], **setting)
    return application

if "__main__" == __name__:
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
