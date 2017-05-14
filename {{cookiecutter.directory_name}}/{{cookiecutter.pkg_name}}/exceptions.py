#!/usr/bin/env python
# coding: utf8

import json
import logging

class HTTP_CODE(object):
    OK = 200
    CREATED = 201
    INTERNAL_SERVER_ERROR = 500


class KMBException(Exception):

    def __init__(self, errdef=None, code=None, msg=None, data=None):
        super(KMBException, self).__init__()
        self._code = code
        self._msg = msg
        self._data = data
        if errdef:
            self._code = errdef.code
            self._msg = errdef.msg

    def __str__(self):
        msg = self._msg.encode('utf-8') if isinstance(self._msg, unicode) else self._msg
        return "BaseException: code=%d, msg='%s'" % (self._code, msg)

    def __eq__(self, other):
        return self._code == other._code

    @property
    def code(self):
        return self._code

    @property
    def msg(self):
        return self._msg

    @property
    def data(self):
        return self._data

    @property
    def info(self):
        return {'error': {'code': self._code,
                          'message': self._msg,
                          'data': self._data}}


class MethodNotAllowed(KMBException):
    def __init__(self, message=u'不支持的HTTP方法'):
        super(MethodNotAllowed, self).__init__(code=405, msg=message)


def exception_handler(func):
    def inner(self, *args, **kwargs):
        self.set_header("Content-Type", "application/json; charset=utf-8")
        try:
            info = func(self, *args, **kwargs)
            if info:
                return self.finish(json.dumps(info, ensure_ascii=False))
            else:
                return self.finish()
        except Exception, e:
            logging.error(e, exc_info=True)
            self.set_status(HTTP_CODE.INTERNAL_SERVER_ERROR)
        return self.finish(json.dumps(e.message, ensure_ascii=False))

    return inner
