#!/usr/bin/env python

"""
#
# Author: sagarbhat94@gmail.com (Sagar Bhat)
#
# This file runs the flask server.
"""

from flask import Flask
from flask_cors import CORS

import env
from py.utils import common_utils as UTILS
from py.utils import constants as CONSTS
from py.utils.logger import Logger

from versions.v1 import blueprint as v1


LOG = Logger.getLogger(__name__)

class FlaskApp(object):
    """Class for configuring and initializing flask app.
    """

    # Class variable for holding the Flask App
    _app = Flask(__name__)

    @classmethod
    def __configure_app(cls):
        """
          Configures the flask app with all necessary configurations.
        """
        cls._app.config["DEBUG"] = CONSTS.FLASK_CONFIG["debug"]

        # Add settings for the swagger and RestPlus modules
        cls._app.config[
            "SWAGGER_UI_DOC_EXPANSION"] = CONSTS.SWAGGER_UI_DOC_EXPANSION
        cls._app.config["RESTPLUS_VALIDATE"] = CONSTS.RESTPLUS_VALIDATE
        cls._app.config[
            "RESTPLUS_MASK_SWAGGER"] = CONSTS.RESTPLUS_MASK_SWAGGER
        cls._app.config["ERROR_404_HELP"] = CONSTS.ERROR_404_HELP

        LOG.debug("Configured flask app successfully.")

    @classmethod
    def __initialize_app(cls):
        """
          Initializes and flask app with required settings.
        """
        # Enable CORS on the flask app
        CORS(cls._app)
        LOG.debug("Enabled CORS on flask app.")


    @classmethod
    def __register_blueprints(cls):
        """Registers blueprints to the flask app.
        """
        # Register blueprints to flask app
        cls._app.register_blueprint(v1)
        LOG.debug("Registered all blueprints to flask app.")

    @classmethod
    def create_app(cls):
        """Class method to set up flask app by:
			1. Configuring the flask app
			2. Initializing the flask app
			3. Registering blueprints to the flask app
        """
        cls.__configure_app()
        cls.__initialize_app()
        cls.__register_blueprints()
        LOG.debug("Class set up complete.")


# Configure and Initialize flask app instance object
flask_app_obj = FlaskApp()
flask_app_obj.create_app()

# Configure secret key for flask app
app = flask_app_obj._app
app.secret_key = "precious"

@app.route("/")
def home():
    """  Default route  """
    return "Hello there. Please refer the API documentation for details."


if __name__ == "__main__":
	app.run(
		host=CONSTS.FLASK_CONFIG["host"],
		port=CONSTS.FLASK_CONFIG["port"])
