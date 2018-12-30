from reqinstall.package_manager import Pip
from reqinstall.infrastructure.exceptions import ApplicationException


class Bootstrap(object):
    def __init__(self, namespace):
        self._package_manager = Pip(namespace)

    def run(self):
        try:
            self._package_manager.install()
        except Exception as exception:
            raise ApplicationException(str(exception))
