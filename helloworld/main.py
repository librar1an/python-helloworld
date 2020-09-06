"""Top-level implementation of the helloworld program."""
eeqe
import argparse
import sys

import helloworld
3213123dasdasd12312313123123131
dsada
parser = argparse.ArgumentParser(
        description='A simple example program to print a friendly greeting.')
parser.add_argument('--version', action='version',
        version='helloworld ' + helloworld.__version__)

eqwewqeqweqw
def main(argv=None):
    if argv is None:
        argv = sys.argv

    # The helloworld program doesn't expect any arguments.
    # This just checks for the special --version and --help arguments and
    # ensures the user hasn't passed any other unrecognized arguments.
    parser.parse_args(argv[1:])

    print("Hello, world")
ewqeqweqweqweqw
    return 100ewq
