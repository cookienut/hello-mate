"""
Author: sagarbhat94@gmail.com (Sagar Bhat)

This file contains the initial environment configuration for Rest APIs.
"""

import os
import sys

assert __name__ != "__main__", "This module should not be executed."

_APP_BASE_DIR_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[
    0]
_APP_BASE_DIR_PATH = os.path.split(_APP_BASE_DIR_PATH)[0]

_APP_INIT_DIR = "py/bin"
_APP_INIT_PATH = os.path.join(_APP_BASE_DIR_PATH, _APP_INIT_DIR)

if os.path.isdir(_APP_INIT_PATH):
    sys.path.insert(0, _APP_INIT_PATH)
    sys.path.insert(0, _APP_BASE_DIR_PATH)
