from dataclasses import dataclass

import logging
from logging.handlers import RotatingFileHandler
import os


log_path = os.environ["PATH_LOG"]

@dataclass
class Logger:

    path: str
    name: str

    def set_logger(self) -> None:

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)

        stream_log = logging.StreamHandler()
        stream_log.setLevel(logging.DEBUG)
        stream_log.setFormatter(formatter)

        self.logger.addHandler(stream_log)

        file_log = RotatingFileHandler(self.path, maxBytes=5 * 1024 * 1024)
        file_log.setLevel(logging.DEBUG)
        file_log.setFormatter(formatter)

        self.logger.addHandler(file_log)

        self.logger.info("LOGGER CONFIGURED")

log_path = os.environ["PATH_LOG"]
logger = Logger(log_path, __name__)
logger.set_logger()