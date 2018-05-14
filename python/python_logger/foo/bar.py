# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)


class FooBar:

    def logger_test(self):
        logger.critical('50 CRITICAL')
        logger.error('40 ERROR')
        logger.warning('30 WARNING')
        logger.info('20 INFO')
        logger.debug('10 DEBUG')
