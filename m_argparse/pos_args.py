import argparse

"""-----------------------------------------------------------------------
Advancing -> Positional arguments
--------------------------------------------------------------------------"""
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="The base")
parser.add_argument("y", type=int, help="The exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0)

args = parser.parse_args()
answer = args.x**args.y

if args.verbosity >= 2:
    print(f"Running '{__file__}'")
elif args.verbosity >= 1:
    print(f"{args.x}^{args.y} == ", end="")
else:
    print(answer)

