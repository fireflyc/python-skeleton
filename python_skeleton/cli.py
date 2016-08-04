import ConfigParser
import click

from python_skeleton.demo import Demo
from python_skeleton.lib import log


@click.command()
@click.option("--config-file", required=True,  default="/etc/python-skeleton/python-skeleton.conf", help="config file", type=click.Path(exists=True))
@click.option("--logging-file", required=True, default="/etc/python-skeleton/python-skeleton-logging.conf", help="logging file", type=click.Path(exists=True))
def main(config_file, logging_file):
    log.setup_logging(logging_file)

    config = ConfigParser.ConfigParser()
    config.read(config_file)
    demo = Demo()
    demo.hello("fireflyc")
m

if __name__ == "__main__":
    import os
    import sys

    parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    etc_path = os.path.join(parent_path, "etc")
    sys.argv.append("--config-file=" + os.path.join(etc_path, "python-skeleton.conf"))
    sys.argv.append("--logging-file=" + os.path.join(etc_path, "python-skeleton-logging.conf"))
    main()
