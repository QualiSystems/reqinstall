import sys
import logging
import subprocess

logger = logging.getLogger(__name__)


# still thinking about whether the run method should accept argument or not
# having thoughts about creating a PipPackages class that knows how to install itself instead of "service" classes
class PipInstallCommand(object):
    def __init__(self, namespace):
        self._install_arguments = self._install_arguments(namespace)

    def run(self):
        # validate pip exists
        arguments = [sys.executable, '-m', 'pip', 'install'] + self._install_arguments
        # logger.info(f"Running {' '.join(arguments)}")  # python 3.6
        logger.info("Running {}".format(' '.join(arguments)))  # should work for python 2 and 3
        return subprocess.call(arguments)

    def _install_arguments(self, namespace):
        arguments = []
        if namespace.packages:
            self._add_argument(arguments, namespace.packages, '')
        if namespace.req_path:
            self._add_argument(arguments, ['-r', namespace.req_path], '')
        if namespace.local_path:
            self._add_argument(arguments, ['--no-index',
                                           '--find-links', '{0}'.format(namespace.local_path)], '')
        if namespace.index_url:
            self._add_argument(arguments, ['--index-url', '{0}'.format(namespace.index_url)], '')
        if namespace.extra_index_url:
            self._add_argument(arguments, ['--extra-index-url', '{0}'.format(namespace.extra_index_url)], '')
        if namespace.trusted_host:
            self._add_argument(arguments, ['--trusted-host', namespace.trusted_host], '')
        if namespace.log:
            self._add_argument(arguments, ['--log', namespace.log], '')
        self._add_argument(arguments, ['--upgrade', '--no-input', '--disable-pip-version-check', '--verbose'], '')
        return arguments

    @staticmethod
    def _add_argument(arguments_list, value, log_message):
        arguments_list += value
        logger.info(log_message)
