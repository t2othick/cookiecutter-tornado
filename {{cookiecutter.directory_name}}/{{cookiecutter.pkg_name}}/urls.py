# coding: utf8

from {{cookiecutter.pkg_name}}.handlers.health import HealthCheckHandler

tests = [
    (r'/check_health', HealthCheckHandler),
]

productions = [
]

handlers = tests + productions
