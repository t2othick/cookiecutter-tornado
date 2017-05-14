#!/usr/bin/env python

import logging
import tornado.autoreload
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
# import tracing.config
from gevent.wsgi import WSGIServer

from {{cookiecutter.pkg_name}}.urls import handlers


def get_tornado_application():
    # tracing.config.initialize()
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
