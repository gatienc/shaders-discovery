'''
Logger configuration module to use in whole project.
'''

import logging
import os
from ..config import DEBUG


def logger_config():
    """
    Configure the logger.

    """
    logger = logging.getLogger('debug')
    logger.setLevel(log_lvl := logging.DEBUG)
    # Creation of a flow manager for the console
    console_handler = logging.StreamHandler()

    # Configuration of the level of journalization of the flow manager
    console_handler.setLevel(log_lvl)
    # Configuration of the format of Journalization Messages
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Addition of the flow manager to the logger
    logger.addHandler(console_handler)
    logger.info('Logger configured')
