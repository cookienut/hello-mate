from logging import getLogger
from flask import make_response, jsonify, Response, request
from flask_restplus import Namespace, Resource, reqparse

from py.models.rest_plus.response import errors, users as user_response
from py.models.objects.users import Users
from py.models.objects.user_history import UserHistory
from py.utils import common_utils as utils
from py.utils import constants, exception


logger = getLogger(__name__)

api = Namespace('users', description='User operations')

# Arguments
parser = reqparse.RequestParser()
parser.add_argument(
    'count', type=int, required=True, default=10, help='For n-top visited websites')
parser.add_argument(
    'start_time', type=int, required=False, help='Start time to specify time range.')
parser.add_argument(
    'end_time', type=int, required=False, help='End time to specify time range')

# Models
error_model = errors.get_error_model(api)
user_show_model = user_response.get_show_model(api)
user_insights_model = user_response.get_insights_model(api)


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
    @api.response(200, 'Success', user_insights_model)
    @api.response(404, 'User not found', error_model)
    @api.expect(parser, validate=True)
    def get(self, uuid):
        """ Generate data insights for user """
        utils.acknowledge_request(request)

        try:
            args = parser.parse_args()
            user = Users(uuid)
            insights = UserHistory(uuid).generate_insights(user, **args)
            utils.acknowledge_response('200')
            return make_response(jsonify(insights))
        except exception.BaseException as e:
            return utils.abort(e.code, message=e.message)
