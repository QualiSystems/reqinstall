import logging
import os
import errno


class CreateHierarchyFileHandler(logging.FileHandler):
    """ Custom file handler that creates the path of the log file if it's not exists """

    def __init__(self, filename, mode='a', encoding=None, delay=0):
        super(CreateHierarchyFileHandler, self).__init__(filename, mode, encoding, delay)
        self._create_path_hierarchy(os.path.dirname(filename))

    @staticmethod
    def _create_path_hierarchy(path):
        try:
            os.makedirs(path)
        except OSError as ex:
            if ex.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise
