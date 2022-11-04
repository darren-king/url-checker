import argparse
from ast import arg

import url_checker


def user_cli_input_args():
    """
    How to deal with user input CLI arguments and options
    """

    parser = argparse.ArgumentParser(
        prog="url_checker", description="check to see if a given URL is online or not"
    )

    parser.add_argument(
        "-u",
        "-urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Please enter the URL of one or more websites.",
    )

    return parser.parse_args()
