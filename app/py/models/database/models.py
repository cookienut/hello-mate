from datetime import datetime

class Users(object):
    """
    Class to store user data.
    """
    _tablename = 'users'

    def __init__(self, uuid, name, email, phone, *args, **kwargs):
        self.uuid = uuid
        self.name = name
        self.email = email
        self.phone = phone
        self.created_at = int(datetime.timestamp())
        self.updated_at = int(datetime.timestamp())

    def __repr__(self):
        return '<Users %r>' % self.user

