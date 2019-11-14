from argparse import ArgumentParser
import logging


__version__ = "0.1"
__appname__ = "".join(__file__.split(".")[:-1])

LOG_FORMAT = "%(asctime)s;%(levelname)s;%(name)s;%(message)s"
LOG_FILE = '{:s}.log'.format(__appname__)
LOG_LEVEL = logging.DEBUG

logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)
logger = logging.getLogger(__appname__)


def main(argv=None):
    args = _args(argv)
    logger.setLevel(args.warn)
    # logger.info("Starting the program.")
    # print(args.warn)
    # print(args.input_file)
    return 0


def _args(argv):
    """ 
    Parse command line arguments.

    :param argv: argument list to parse
    """
    parser = ArgumentParser()
    parser.add_argument("-v", "--version", action="version",
                        version="{:s} {:s}".format(__appname__, __version__),
                        help="print version and exit")
    parser.add_argument("-w", "--warn", default="DEBUG", choices=["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"],
                        help="logger warning level [DEBUG]")
    parser.add_argument("-i", "--input_file", help="path to input file")
    # parser.add_argument("-c", "--config", action="append",
    #                     help="config file [etc/config.yml]")
    # common = ArgumentParser(add_help=False)  # common subcommand arguments
    # common.add_argument("--name", "-n", default="World", help="greeting name")
    # subparsers = parser.add_subparsers(title="subcommands")
    # _hello(subparsers, common)
    args = parser.parse_args(argv)
    # if not args.config:
    #     # Don't specify this as an argument default or else it will always be
    #     # included in the list.
    #     args.config = "etc/config.yml"

    return args


if __name__ == "__main__":
    raise SystemExit(main())
