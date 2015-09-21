__author__ = 'veradocs-web'

import logging
# By default, informational and debugging messages are suppressed and the output is sent to standard error.
# New filters can select different routing based on message priority: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

