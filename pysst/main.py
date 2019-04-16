from behave.__main__ import main as behave_main
from pysst.steps import *
import argparse
import os
import shutil
import sys


def main():
    parser = argparse.ArgumentParser(description='Run one or more pysst test suites')
    parser.add_argument('--features', nargs='+', help='Path to your feature(s)')
    parser.add_argument('--init', help='Directory or Directories of your features')
    args = parser.parse_args()
    if args.init is not None:
        create_skeleton(args.init)
    else:
        launch_behave(args.features)

def launch_behave(features):
    try:
        for feature in features:
            sys.exit(behave_main(feature))
    except TypeError:
        sys.exit(behave_main())


def create_skeleton(path):
    root = os.path.dirname(os.path.realpath(__file__))
    shutil.copytree(f'{root}/skeleton', path)


if __name__ == "__main__":
    main()
