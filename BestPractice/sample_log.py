#test python logging facility
import logging

logging.basicConfig(filename="sample.log",level=logging.DEBUG)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')