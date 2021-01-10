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

    @staticmethod
    def _from_db_object(db_obj):
        """Converts a database entity to a formal object."""
        user = dict()
        for field in Users.fields:
            user[field] = db_obj.get(field)
        return user

    @staticmethod
    def _from_db_object_list(db_objects):
        """Converts a list of db entities to a list of formal objects."""
        return [
            Users._from_db_object(obj) for obj in db_objects
        ]

    def get(self):
        """ Get a user from Mongo Atlas DB """
        user = self.records.find_one({'uuid': self.uuid})
        return Users._from_db_object(user)
