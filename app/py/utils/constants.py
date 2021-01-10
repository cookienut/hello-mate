"""
# Author: sagarbhat94@gmail.com (Sagar Bhat)
#
# This file contains all the constant values and mappings that are used
# throughout this project.
"""

from json import load
from os import path

# Generate path to configuration directory
_DIR_PARENT_PATH = path.split(path.abspath(path.dirname(__file__)))[0]
_CONFIG_BASE_DIR = path.join(path.split(_DIR_PARENT_PATH)[0], "config")

# Read configuration file
CONFIG = load(open(path.join(_CONFIG_BASE_DIR, "config.json")))

# MongoDB Atlas Settings
MONGO_CONFIG = CONFIG["mongo_atlas"]
MONGODB_DB_NAME = MONGO_CONFIG["database"]
MONGODB_ATLAS_URI = (
    f'mongodb+srv://{MONGO_CONFIG["username"]}:{MONGO_CONFIG["password"]}@'
    f'cluster0.mgqk9.mongodb.net/{MONGODB_DB_NAME}?retryWrites=true&w=majority'
)

# Logger related configuration
LOG_CONFIG = CONFIG["logging"]

# Flask realted configuration
FLASK_CONFIG = CONFIG["flask"]

# Swagger related configuration
SWAGGER_UI_DOC_EXPANSION = "list"
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
ERROR_404_HELP = False
