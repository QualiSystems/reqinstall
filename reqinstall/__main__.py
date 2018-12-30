import sys
import logging
import argparse

from reqinstall.bootstrap import Bootstrap
from reqinstall.infrastructure.logs import configure_file_appender, configure_stream_appender
from reqinstall.infrastructure.exceptions import ApplicationException

logger = logging.getLogger()


def main():
    arguments = argparse.ArgumentParser(description="CloudShell utility that manages scripts requirements installation",
                                        formatter_class=argparse.RawTextHelpFormatter)
    install_group = arguments.add_mutually_exclusive_group(required=True)
    local_group = arguments.add_argument_group()

    arguments.add_argument('--index-url', '-i', dest='index_url', required=False,
                           help="The index to look for packages. Usually configured to pypi")
    arguments.add_argument('--trusted-host', '-th', dest='trusted_host', required=False,
                           help="The base url of the trusted host address index. "
                                "Mainly for private repository use cases")
    arguments.add_argument('--extra-index-url', '-xurl', dest='extra_index_url', nargs='*', required=False,
                           help="Extra indexes urls for multiple repositories")
    arguments.add_argument('--log', '-l', dest="log", required=False, help="Log path")
    install_group.add_argument('--req_file', '-r', dest='req_path',
                               help="Path to a file containing packages to install. Usually named requirements.txt")
    install_group.add_argument('--packages', '-p', dest='packages', nargs='*',
                               help="List of packages to install separated by spaces")
    local_group.add_argument('--local-path', '-lp', dest='local_path',
                             help="Path to folder containing packages locally")  # deprecated by pypi server commit

    exit_code = 1
    try:
        namespace = arguments.parse_args()
        configure_logging(namespace)
        Bootstrap(namespace).run()
        exit_code = 0
    except ApplicationException as exception:
        logger.error('Failed with error: {}'.format(str(exception)), exc_info=exception)
    except Exception as exception:
        logger.error("Failed", exc_info=exception)
    finally:
        sys.exit(exit_code)


def configure_logging(namespace):
    if namespace.log:
        configure_file_appender(namespace.log)
    else:
        configure_stream_appender()


# def main(**kwargs):
#
#     pass

if __name__ == "__main__":
    main()

