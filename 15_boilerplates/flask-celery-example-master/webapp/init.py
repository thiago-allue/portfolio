""" Reads config files and setups logger. """

import os
import sys
import time
import logging
import logging.config
import yaml

here = os.path.dirname(os.path.abspath(__file__))


def init():
    """
    Sets up this module's globals accessible from the rest of the application:

    - logger (logging)
    - credentials (dict)
    - config (dict)
    """
    global logger
    logs_path = os.path.join(here, 'logs')
    if not os.path.isdir(logs_path):
        os.makedirs(logs_path, exist_ok=True)

    logging_config = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] - %(levelname)8s - %(filename)s - %(message)s',
            },
            'detailed': {
                'format': ('[%(asctime)s] - %(levelname)8s - [%(filename)s:%(funcName)s:%(lineno)d]'
                        ' - [%(process)d:%(processName)s | %(thread)d:%(threadName)s] - %(message)s'),
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'detailed',
                'level': 'DEBUG'
            },
            'logfile': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'formatter': 'detailed',
                'filename': os.path.join(logs_path, 'portal-app.log'),
                'mode': 'a'
            },
            'debuglogfile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'detailed',
                'filename': os.path.join(logs_path, 'portal-app-DEBUG.log'),
                'mode': 'a',
                'maxBytes': 10 * 1024 * 1024,
                'backupCount': 1000,
            },
        },
        'loggers': {
            '': {
                'handlers': ['debuglogfile', 'console', 'logfile'],
                'level': 'DEBUG'
            },
        }
    }
    logging.Formatter.converter = time.gmtime
    logging.config.dictConfig(logging_config)
    logger = logging
    logger.info('Logging setup executed.')

    try:
        global credentials
        global config
        with open(os.path.join(os.path.join(here, 'config'), 'credentials.yaml'), 'r') as f:
            credentials = yaml.load(f)
            logger.debug('Credentials loaded successfully')
        with open(os.path.join(os.path.join(here, 'config'), 'app.yaml'), 'r') as cfg:
            config = yaml.load(cfg)
            logger.debug('Configuration loaded successfully')
    except Exception as e:
        logger.exception('Reading configuration files failed.')
        sys.exit(1)


def reload_credentials():
    global credentials
    with open(os.path.join(os.path.join(here, 'config'), 'credentials.yaml'), 'r') as f:
        credentials = yaml.load(f)
        logger.debug('Credentials reloaded successfully')


def reload_config():
    global config
    with open(os.path.join(os.path.join(here, 'config'), 'app.yaml'), 'r') as cfg:
        config = yaml.load(cfg)
        logger.debug('Configuration reloaded successfully')


if __name__ == '__main__':
    logger.debug('Running config directly')
