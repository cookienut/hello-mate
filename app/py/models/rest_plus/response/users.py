from flask_restplus import fields


def get_show_model(api):
    """ Return show model for response """
    show_model = api.model('User Show', {
        'uuid': fields.String(required=True, description='User UUID'),
        'name': fields.String(required=True, description='User name'),
        'email': fields.String(required=True, description='User email'),
        'phone': fields.String(required=True, description='User phone number'),
        'created_at': fields.String(required=True, description='Creation time'),
        'updated_at': fields.String(required=True, description='Updation time')
    })
    return show_model
