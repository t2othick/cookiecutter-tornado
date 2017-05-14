#!/usr/bin/env python

from {{cookiecutter.pkg_name}}.exceptions import exception_handler, HTTP_CODE, MethodNotAllowed

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    def get_url(self, path, param=None, query_params=None):
        """Get url.
        """
        schema = self.request.headers.get('X-Scheme', None) or \
            self.request.protocol

        url = '{0}://{1}{2}'.format(
            schema, self.request.host, path)

        if param:
            url = '{0}/{1}'.format(url, param)

        if query_params:
            url = url + '?' + query_params

        return url

    def get_int_argument(self, name, default=None):
        arg = self.get_argument(name, '')
        if arg.isdigit():
            return int(arg)
        else:
            return default

    @exception_handler
    def get(self, *args, **kwargs):
        return self.real_get(*args, **kwargs)

    def real_get(self, *args, **kwargs):
        raise MethodNotAllowed()

    @exception_handler
    def post(self, *args, **kwargs):
        self.set_status(HTTP_CODE.CREATED)
        return self.real_post(*args, **kwargs)

    def real_post(self, *args, **kwargs):
        raise MethodNotAllowed()

    @exception_handler
    def put(self, *args, **kwargs):
        self.set_status(HTTP_CODE.ACCEPTED)
        return self.real_put(*args, **kwargs)

    def real_put(self, *args, **kwargs):
        raise MethodNotAllowed()

    @exception_handler
    def delete(self, *args, **kwargs):
        return self.real_delete(*args, **kwargs)

    def real_delete(self, *args, **kwargs):
        raise MethodNotAllowed()

    @exception_handler
    def patch(self, *args, **kwargs):
        return self.real_patch(*args, **kwargs)

    def real_patch(self, *args, **kwargs):
        raise MethodNotAllowed()

    def finish(self, chunk=None):
        self._chunk = chunk
        self.set_header("Content-Type", "application/json; charset=utf-8")

        if self._auto_finish and not self._finished:
            RequestHandler.finish(self, self._chunk)
