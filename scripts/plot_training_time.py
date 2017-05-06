# -*- coding: utf-8 -*-
""" Script for plotting trianing time of pose net. """

import argparse
import sys

sys.path.append("./")
from modules.evaluators import TrainingTimeEvaluator


def main():
    """ Main function. """
    # arg definition
    parser = argparse.ArgumentParser(
        description='Training time comparison of pose net between chainer and pytorch.')
    parser.add_argument(
        'title', type=str, help='Title of comparison graph.')
    parser.add_argument(
        '--chainer-logs', '-c', nargs='+', type=str, default=[], help='Space separated log files of chainer.')
    parser.add_argument(
        '--pytorch-logs', '-p', nargs='+', type=str, default=[], help='Space separated log files of pytorch.')
    parser.add_argument(
        '--output', default='result', help='Output directory.')
    parser.add_argument(
        '--debug', action='store_true', help='Debug mode.')
    args = parser.parse_args()
    evaluator = TrainingTimeEvaluator(args.chainer_logs, args.pytorch_logs, args.output)
    evaluator.plot(args.title, args.debug)


if __name__ == '__main__':
    main()
