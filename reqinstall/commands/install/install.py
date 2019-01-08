import sys
import logging
import subprocess

logger = logging.getLogger(__name__)


class PipInstallCommand(object):
    def run(self, namespace):
        arguments = [sys.executable, '-m', 'pip', 'install'] + self._install_arguments(namespace)
        logger.info("Running {}".format(' '.join(arguments)))
        return subprocess.call(arguments)

    def _install_arguments(self, namespace):
        arguments = []
        if namespace.packages:
            self._add_argument(arguments, namespace.packages)
        if namespace.req_path:
            self._add_argument(arguments, ['-r', namespace.req_path])
        if namespace.local_path:
            self._add_argument(arguments, ['--no-index',
                                           '--find-links', '{0}'.format(namespace.local_path)])
        if namespace.index_url:
            self._add_argument(arguments, ['--index-url', '{0}'.format(namespace.index_url)])
        if namespace.extra_index_url:
            self._add_argument(arguments, ['--extra-index-url', '{0}'.format(namespace.extra_index_url)])
        if namespace.trusted_host:
            self._add_argument(arguments, ['--trusted-host', namespace.trusted_host])
        if namespace.log:
            self._add_argument(arguments, ['--log', namespace.log])
        self._add_argument(arguments, ['--upgrade', '--no-input', '--disable-pip-version-check', '--verbose'])
        return arguments

    @staticmethod
    def _add_argument(arguments_list, value):
        arguments_list += value
