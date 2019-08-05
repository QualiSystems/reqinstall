import os
import sys
import logging
import subprocess

logger = logging.getLogger(__name__)


class PipInstallCommand(object):
    def run(self, namespace):
        try:
            with open(namespace.req_path, 'r') as f:
                requirements = f.read()
            logger.info('we are about to install the following packages:{linesep}'
                         '{packages}'.format(linesep=os.linesep, packages=requirements))
        except Exception:
            pass
        arguments = [sys.executable, '-m', 'pip', 'install'] + self._install_arguments(namespace)
        logger.info("Running {}".format(' '.join(arguments)))
        return subprocess.call(arguments)

    @staticmethod
    def _install_arguments(namespace):
        arguments = []
        if namespace.packages:
            arguments += namespace.packages
        if namespace.req_path:
            arguments += ['-r', namespace.req_path]
        if namespace.local_path:
            arguments += ['--no-index', '--find-links', '{0}'.format(namespace.local_path)]
        if namespace.index_url:
            arguments += ['--index-url', '{0}'.format(namespace.index_url)]
        if namespace.extra_index_url:
            for index_url in namespace.extra_index_url:
                arguments += ['--extra-index-url', index_url]
        if namespace.trusted_host:
            arguments += ['--trusted-host', namespace.trusted_host]
        if namespace.log:
            arguments += ['--log', namespace.log]
        arguments += ['--upgrade', '--no-input', '--disable-pip-version-check', '--verbose']
        return arguments
