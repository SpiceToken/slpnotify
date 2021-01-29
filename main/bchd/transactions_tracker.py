
import logging
import sys

# sys.path.append('/code/main/bchd/protobuf')
logger = logging.getLogger(__name__)


class TransactionsTracker(object):

    def run(self):
        logger.info('Tracking transactions...')
