from flask import Blueprint
from flask import url_for
from flask_restplus import Api

from py.controllers.v1.users import api as users


blueprint = Blueprint('HelloM8', __name__, url_prefix='/v1')

# Add doc=False below to disable to Swagger UI
api = Api(
    blueprint,
    title="Hello M8",
    version='v1',
    description="This page covers all the accessible version1 (v1) REST APIs.",
    # Add more API metadatas
    )

api.add_namespace(users)