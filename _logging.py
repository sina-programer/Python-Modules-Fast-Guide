import logging

logging.basicConfig(
    filename='Log.log',
    encoding='utf-8',
    filemode='w',
    format='%(asctime)s %(message)s'
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.log(logging.WARNING, 'Warning Sample')
logger.debug('Debug Message')
logger.info('Information')
logger.warning("It's a Warning")
logger.error('Error Logging')
logger.critical('Critical!')
