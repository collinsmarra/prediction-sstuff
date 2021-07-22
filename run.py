#!/usr/bin/env python3


from program import  Traintest
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--train", help="provide data for tarining")
parser.add_argument("--test", help="provide data to be tested")
parser.add_argument("-o", "--output", help="output file")
args = parser.parse_args()


if __name__ == "__main__":
    try:
        qq = Traintest(args.train, args.test, args.output)
        qq.trainer()
        qq.testing()
        qq.back_to_df()
        qq.combine_data()
    except KeyboardInterrupt:
        sys.exit(0)


