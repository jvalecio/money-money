import rich
import argparse
from core.base import interest

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    subsparser = parser.add_subparsers(help='s help')

    parser_interest = subsparser.add_parser('interest',help='a help')
    parser_interest.add_argument("-j", type=float)
    parser_interest.add_argument("-c", type=float)
    parser_interest.add_argument("-n", type=int)
    parser_interest.add_argument("-r", type=float)
    parser_interest.set_defaults(func=interest)

    args = parser.parse_args()
    print(args.func(args))

