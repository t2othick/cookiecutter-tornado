#!/usr/bin/env python
#
# Copyright 10/05/2017 Zhihu
# Author: hdd
# FileName: app.py
# Project: zhihu-live
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

""" Web app work with tornado
"""
import logging
import tornado.autoreload
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import tracing.config
from gevent.wsgi import WSGIServer

from kmb.urls import handlers

from kmb.logger import add_logging_handler


def get_tornado_application():
    tracing.config.initialize()
    settings = dict(
        version='3.0.35',
        gzip=True,
        debug=True,
        cookie_secret='ulhDhutRkBDJj0WN6loZTJ',
        xsrf_cookie=True,
    )
    application = tornado.web.Application(handlers, **settings)
    return application


def get_wsgi_application():
    tornado_application = get_tornado_application()
    return tornado.wsgi.WSGIAdapter(tornado_application)


def run():
    port = 3000
    wsgi_server = WSGIServer(('', port), get_wsgi_application())
    logging.info('listening on {port}'.format(port=3000))
    wsgi_server.serve_forever()


if __name__ == '__main__':
    run()
