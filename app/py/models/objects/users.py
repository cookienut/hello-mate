#!/usr/bin/env python

from datetime import datetime
from py.models.objects.base import MongoBaseClass


class Users(MongoBaseClass):

    fields = [
        'uuid', 'name', 'email', 'created_at', 'updated_at', 'phone'
        ]

    def __init__(self, uuid):
        self.uuid = uuid
        self.collection = 'users'
        self.records = getattr(self.db_client_obj, self.collection)

    def get(self):
        """ Get a user from Mongo Atlas DB """
        user = self.records.find_one({'uuid': self.uuid})
        return self._from_db_object(user, fields=Users.fields)
