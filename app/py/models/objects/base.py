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
 
