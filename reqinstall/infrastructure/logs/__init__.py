import sys
import logging

from reqinstall.infrastructure.logs.custom_file_handler import CreateHierarchyFileHandler

GLOBAL_LOG_LEVEL = logging.INFO


def configure_file_appender(file_path):
    logger = logging.getLogger()
    logger.setLevel(GLOBAL_LOG_LEVEL)
    formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    fh = CreateHierarchyFileHandler(file_path)
    fh.setFormatter(logging.Formatter(formatter))
    logger.addHandler(fh)


def configure_stream_appender():
    logger = logging.getLogger()
    logger.setLevel(GLOBAL_LOG_LEVEL)
    formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(logging.Formatter(formatter))
    logger.addHandler(sh)
