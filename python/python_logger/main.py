#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import logging.config

logger = logging.getLogger(__name__)
logging.config.fileConfig('logging.ini', disable_existing_loggers=False)


if __name__ == "__main__":
    logger.critical('50 CRITICAL')
    logger.error('40 ERROR')
    logger.warning('30 WARNING')
    logger.info('20 INFO')
    logger.debug('10 DEBUG')

    from foo import bar
    bar.FooBar().logger_test()

