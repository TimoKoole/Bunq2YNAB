import argparse
import os

from bunq2ynab.converter import Converter

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input file, default transactions.csv', type=str, nargs='?',
                        default=os.path.join(os.getcwd(), "transactions.csv"))
    parser.add_argument('-o', '--output', help='output file, default bunq.csv', type=str, nargs='?',
                        default=os.path.join(os.getcwd(), "bunq.csv"))
    args = parser.parse_args()
    print("Converting file: " + args.input)

    converter = Converter(args.input)
    converter.convert()
    converter.write_outputfile(args.output)
