#!/usr/bin/env python


class BaseException(Exception):
    message = "An unknown exception occurred, please check Chaos REST-API logs"
    code = 500

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs
        if 'code' not in self.kwargs:
            try:
                self.kwargs['code'] = self.code
            except AttributeError:
                pass
        if message:
            self.message = message

        try:
            self.message = self.message % kwargs
        except Exception as e:
            raise e
        super(BaseException, self).__init__(self.message)


class NotFound(BaseException):
    code = 404

    def __init__(self, resource, name):
        self.message = "No {} found with name: '{}'" \
            .format(resource.title(), name)


class InvalidCredentials(BaseException):
    code = 401

    def __init__(self, resource, name):
        self.message = "Invalid credentials for user with {} as: '{}'".format(
            resource.title(), name)

class UserFoundError(BaseException):
    code = 408

    def __init__(self, resource, name):
        self.message = "Mobile number already exists."

class UserNotFound(BaseException):
    code = 408

    def __init__(self, resource, name):
        self.message = "Mobile number not registered."

class BaseError(BaseException):
    code = 506

    def __init__(self, resource, name):
        self.message = "Error in {} resource with name: '{}'" \
            .format(resource.title(), name)

class CustomError(BaseException):
    code = 506

    def __init__(self, message):
        self.message = message 
