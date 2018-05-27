#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import logging

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

class Watcher:

    def __init__(self):
        self.observer = Observer()
        self.handler = LoggingEventHandler()
        self.directory = sys.argv[1] if len(sys.argv) > 1 else '.'
        self.date_format = '%Y-%m-%d %H:%M:%S'

    def run(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt=self.date_format
        )
        self.observer.schedule(self.handler, self.directory, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


if __name__ == "__main__":
    Watcher().run()
