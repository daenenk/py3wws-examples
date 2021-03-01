"""Main entrypoint into the package"""

import argparse
from py3wws.wrap import wws_start, add_setup_options


def setup_argparser() -> argparse.ArgumentParser:
    """Setup a custom argument parser for this package."""
    argp = argparse.ArgumentParser()
    add_setup_options(argp)
    return argp


def main() -> None:
    """Start the processor using the custom argument parser."""
    argp = setup_argparser()
    args = argp.parse_args()
    kwargs = vars(args)

    # Set the default queue if not specified with a command line argument.
    kwargs['config.processor.queue_name'] = kwargs.get('config.processor.queue_name') or 'py3wws/examples'
    wws_start(no_argparse=True, **kwargs)


main()
