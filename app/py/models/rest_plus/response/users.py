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


def get_insights_model(api):
    """ Return insights model for response """
    history_fields = api.model("History Model", {
        'url': fields.String(description='Visited url'),
        'visits': fields.Integer(description='Frequency of visits'),
        'tags': fields.List(fields.String, description='Additional tags')
    })

    insights_model = api.model('User Insights', {
        'uuid': fields.String(required=True, description='User UUID'),
        'name': fields.String(required=True, description='User name'),
        'email': fields.String(required=True, description='User email'),
        'history': fields.List(
            fields.Nested(history_fields),
            required=True,
            description='Browsing insights')
    })
    return insights_model
