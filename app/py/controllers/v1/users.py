from logging import getLogger
from flask import make_response, jsonify, Response, request
from flask_restplus import Namespace, Resource

from py.models.rest_plus.response import errors, users as user_response
from py.models.objects.users import Users
from py.utils import common_utils as utils
from py.utils import constants, exception

logger = getLogger(__name__)

api = Namespace('users', description='User operations')

role_args = api.parser()
role_args.add_argument('role', type=str, required=True,
                       choices=['guard', 'society_admin', 'admin'],
                       default='guard')

error_model = errors.get_error_model(api)
user_show_model = user_response.get_show_model(api)


@api.route('/<string:uuid>')
@api.response(506, 'Failed to perform request', error_model)
@api.param('uuid', 'The user UUID identifier')
class UsersController(Resource):
    @api.response(200, 'Success', user_show_model)
    @api.response(404, 'User not found', error_model)
    def get(self, uuid):
        """ Fetch a user based on UUID """
        utils.acknowledge_request(request)

        # uuid format: 89a97b2c-f25c-4abc-bc38-fe28d0070c02
        user = Users(uuid)
        try:
            user_info = user.get()
            utils.acknowledge_response('200')
            return make_response(jsonify(user_info))
        except exception.BaseException as e:
            return utils.abort(e.code, message=e.message)

@api.route('/<string:uuid>/insights')
@api.response(506, 'Failed to perform request', error_model)
@api.param('uuid', 'The user UUID identifier')
class UserInsightController(Resource):
    @api.response(200, 'Success', user_show_model)
    @api.response(404, 'User not found', error_model)
    def get(self, uuid):
        """ Generate data insights for user """
        utils.acknowledge_request(request)

        user_info = Users(uuid).get()
        try:
            insights = {"message": f"Data Insights!{user_info}"}  # user.get()
            utils.acknowledge_response('200')
            return make_response(jsonify(insights))
        except exception.BaseException as e:
            return utils.abort(e.code, message=e.message)
