"""
# Author: sagarbhat94@gmail.com (Sagar Bhat)
#
# This file contains the base logger for CHAOS project.
#
"""

import os
import time

from logging.handlers import RotatingFileHandler
import logging

from py.singleton import Singleton
from py.utils import constants as CONSTS


class Logger(object):
    """
      Logging class
    """
    _logger = None
    __metaclass__ = Singleton

    @classmethod
    def _validate_log_dir(cls):
        """
          Validate if the log directory exists or not.
          If directory doesn't exist, creates the log directory.
        """
        log_dir = os.path.dirname(CONSTS.LOG_CONFIG["log_file"])
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

    @classmethod
    def _getLogLevel(cls, log_level):
        """
          Method to return log level.
        """
        __logging_levels = {
            "INFO": logging.INFO,
            "DEBUG": logging.DEBUG,
            "ERROR": logging.ERROR,
        }
        return __logging_levels[log_level]

    @classmethod
    def getLogger(cls, *args, **kwargs):
        """
          Get Logger object
        """
        if cls._logger:
            return cls._logger

        cls._validate_log_dir()

        logger = logging.getLogger(*args, **kwargs)
        file_handler = RotatingFileHandler(
            filename=CONSTS.LOG_CONFIG["log_file"],
            maxBytes=1024 * 1024,
            backupCount=10)

        log_format = r"[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
        formatter = logging.Formatter(log_format)
        formatter.converter = time.localtime
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(cls._getLogLevel(CONSTS.LOG_CONFIG["log_level"]))

        cls._logger = logger
        return cls._logger
