import os
import logging

from reqinstall.package_manager import Pip
from reqinstall.infrastructure.exceptions import ApplicationException

logger = logging.getLogger(__name__)


class Bootstrap(object):
    def __init__(self, namespace):
        self._package_manager = Pip(namespace)
        # log current environment snapshot by using pip freeze command
        logger.info('environment snapshot:{linesep}'
                    '{snapshot}'.format(linesep=os.linesep, snapshot=self._package_manager.freeze()))

    def run(self):
        try:
            return self._package_manager.install()
        except Exception as exception:
            raise ApplicationException(str(exception))
