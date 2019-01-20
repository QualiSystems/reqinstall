import logging

from reqinstall.commands.install import PipInstallCommand

logger = logging.getLogger(__name__)


class Pip(object):
    def __init__(self, namespace):
        self._namespace = namespace

    def install(self):
        return PipInstallCommand().run(self._namespace)
