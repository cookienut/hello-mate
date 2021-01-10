#!/usr/bin/env python

"""
#
# Author: sagarbhat94@gmail.com (Sagar Bhat)
#
# This file will populate the MongoDB Atlas Cloud DB with expected data.
"""

import uuid
import random
import pathlib
import datetime

import xlrd
from pymongo import MongoClient


DATABASE_NAME = ""
DATABASE_PASS = ""
MONGODB_ATLAS_URI = (
    f"mongodb+srv://test:{DATABASE_PASS}@cluster0.mgqk9."
    f"mongodb.net/{DATABASE_NAME}?retryWrites=true&w=majority")

# User names
USERS = ["Sagar", "Kirit", "Arjun", "Johann"]
# User creation date range: Jan 01, 2019 - Jan 01, 2020 in epoch milliseconds
DATES = range(1546300800000, 1577836800000, 86400000)
# Country code and phone numbers
COUNTRY_CODE = ["+61", "+91"]
PHONE_NUMBER = range(9100000000, 9900000000, 456789)


def read_xlsx(filename):
    _path = pathlib.Path(__file__).resolve().parent
    file_path = pathlib.Path.joinpath(_path, filename)
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)
    return sheet

def db_connect():
    client = MongoClient(MONGODB_ATLAS_URI)
    return client.get_database(DATABASE_NAME)

def get_documents(conn, collection_name):
    return getattr(conn, collection_name)

def add_users(conn):
    user_docs = []
    for user in USERS:
        creation_time = random.choice(DATES)
        _doc = {
            'uuid': str(uuid.uuid4()),
            'name': user,
            'created': creation_time,
            'last_updated': creation_time,
            'phone': f"{random.choice(COUNTRY_CODE)}-{random.choice(PHONE_NUMBER)}"
        }
        user_docs.append(_doc)
    records = get_documents(conn, "users")
    print(records.insert_many(user_docs))

def add_browsing_data(conn):
    user_data = []
    for user in get_users(conn):
        user_data.append((user["uuid"], user["created"]))

    # Read from xlsx
    sheet=read_xlsx("browsing_history_multiple_users.xlsx")
    history = []
    records = get_documents(conn, collection_name="browsing_history")
    for rowx in range(sheet.nrows):
        _, url = sheet.row_values(rowx)
        user_uuid, min_time = random.choice(user_data)
        date_range = range(min_time, 1609459200000, 86400000)
        browse_time = random.choice(date_range)
        _doc = {
            'uuid': user_uuid,
            'url': url,
            'time': browse_time
        }
        history.append(_doc)
    # Insert records in Mongo Atlas DB
    records.insert_many(history)

def get_users(conn, uuid=None):
    records = get_documents(conn, collection_name="users")
    if uuid:
        return records.find_one({"uuid": uuid})
    return records.find({})


if __name__ == "__main__":

    conn = db_connect()
    # 1. Add users
    add_users(conn)
    print("Users generated.")
    # 2. Add browsing data from xlsx file
    add_browsing_data(conn)
    print("Browsing data generated")

    print("Done.")

    # updated = {"date": datetime(2021, 1, 1, 18, 30)}
    # records.update_one({"user_id": 2}, {"$set": updated})
    # records.update_many({"user_id": 2}, {"$set": updated})
    # records.insert_one(new_history)
    # records.insert_many([new_history1, new_history2...])
    # records.find() - returns cursor object, need to call next
    # or typecast to list
    # list(records.find()) - returns all
    # x = records.find_one({"user_id": 1})
    # x = records.delete_one({"user_id": 2})
