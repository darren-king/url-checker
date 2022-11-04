import argparse
from ast import arg

import url_checker


def user_cli_input_args():
    """
    How to deal with user input CLI arguments and options.
    """

    parser = argparse.ArgumentParser(
        prog="url_checker", description="check to see if a given URL is online or not"
    )

    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],  # sets the command-line argument to an empty list by default
        help="Please enter the URL of one or more websites.",
    )

    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )

    return (
        parser.parse_args()
    )  # returns a Namespace object containing the parsed arguments


def display_check_results(result, url, error=""):
    """
    Display the result of the URL connectivity check.
    """

    print(f'"{url}" is:', end=" ")
    if result:
        print("Online!")
    else:
        print(f'"Offline??" \n Error: "{error}"')
