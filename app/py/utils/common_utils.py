import json

from flask import Response
from py.utils.logger import Logger

LOG = Logger.getLogger()


def abort(code, **kwargs):
    """ Create custom abort responses to dispatch failed requests """
    description = json.dumps(kwargs)
    LOG.error("[ERROR]: {}; Status Code: {}".format(description, code))
    return Response(status=code, mimetype='application/json',
                    response=description)


def acknowledge_request(request):
    """ Log request """
    LOG.info("Received [{}] request from client: [{}] on url [{}]".format(
        request.method, request.remote_addr, request.url))


def acknowledge_response(status_code):
    """ Log response """
    LOG.info("Dispatched response with status code: {}".format(status_code))
