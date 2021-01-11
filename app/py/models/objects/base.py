#!/usr/bin/env python

from pymongo import MongoClient

from py.utils import constants as CONSTS

class MongoBaseClass(object):

    mongo_db_conn_obj = None

    @property
    def db_client_obj(self):
        if not self.mongo_db_conn_obj:
            self.mongo_db_conn_obj = MongoClient(CONSTS.MONGODB_ATLAS_URI)
        return self.mongo_db_conn_obj.get_database(CONSTS.MONGODB_DB_NAME)
 
    @staticmethod
    def _from_db_object(db_obj, fields):
        """Converts a database entity to a formal object."""
        formal_obj = dict()
        for field in fields:
            formal_obj[field] = db_obj.get(field)
        return formal_obj

    @staticmethod
    def _from_db_object_list(db_objects, fields):
        """Converts a list of db entities to a list of formal objects."""
        return [
            MongoBaseClass._from_db_object(obj, fields) for obj in db_objects
        ]
