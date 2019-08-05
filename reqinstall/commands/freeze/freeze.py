import os
import sys
import platform
import logging
import subprocess

logger = logging.getLogger(__name__)


class PipFreezeCommand(object):
    def run(self):
        arguments = [sys.executable, '-m', 'pip', 'freeze']
        logger.info("Running {}".format(' '.join(arguments)))

        try:
            dependencies_snapshot = subprocess.check_output(arguments)
            dependencies_snapshot = dependencies_snapshot if type(
                dependencies_snapshot) is str else dependencies_snapshot.decode()  # py 3 check_output is bytes vs str

            # replace line separator on non linux machines
            system_name = platform.system()
            if system_name and system_name.lower() != 'linux':
                dependencies_snapshot = dependencies_snapshot.rstrip().replace('\r\n', os.linesep)

            return dependencies_snapshot.strip()
        except Exception:
            logger.warning('cannot print environment snapshot due to a failure in pip freeze')
            logger.exception('captured exception')