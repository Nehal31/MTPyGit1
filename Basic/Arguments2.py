# Execution Arguments2.py arg1 arg2 ...

import argparse

def main():
    description = 'Math operation'
    args_parser = argparse.ArgumentParser(description=description)
    args_parser.add_argument("num1", help="Number 1", type=float, default=0.0)
    args_parser.add_argument("--num2", help="Number 2", type=float, default=0.0)
    args_parser.add_argument("--operation", help="Math Operator", type=str, default='+')
    args = args_parser.parse_args()
    if args.operation == '+':
        print(args.num1 + args.num2)

    print(args)


if __name__ == '__main__':
    main()
