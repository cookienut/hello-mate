from flask_restplus import fields


def get_error_model(api):
    """ Return error model for its response """
    error_info = api.model('Error Response', {
        'message': fields.String(required=True, description='Error Message')
    })
    return error_info
