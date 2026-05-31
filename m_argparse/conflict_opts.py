import argparse

"""-----------------------------------------------------------------------
Conflicting Options
--------------------------------------------------------------------------"""
# Introducing **add_mutually_exclusive_group()** -> lets us specify options that
# conflict with each other.
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true", help="increase verbosity of the output")
group.add_argument("-q", "--quiet", action="store_true", help="limit the output\'s verbosity")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

args = parser.parse_args()
answer = args.x**args.y


if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power of {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")