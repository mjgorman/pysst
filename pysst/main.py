from behave.__main__ import main as behave_main
from pysst.steps import *
import argparse
import os
import shutil
import sys


def main():
    parser = argparse.ArgumentParser(description='Run one or more pysst test suites')
    parser.add_argument('-f', '--features', nargs='+', help='Path to your feature(s)')
    parser.add_argument('-i', '--init', help='Directory or Directories of your features')
    args = parser.parse_args()
    if args.init:
        create_skeleton(args.init)
    elif args.features:
        launch_behave(args.features)
    else:
        parser.print_help()

def launch_behave(features):
    try:
        for feature in features:
            sys.exit(behave_main(feature))
    except TypeError:
        sys.exit(behave_main())


def create_skeleton(path):
    root = os.path.dirname(os.path.realpath(__file__))
    try:
        shutil.copytree(f'{root}/skeleton', path)
    except FileExistsError:
        print(f'ERROR: {path} directory already exists.')


if __name__ == "__main__":
    main()
