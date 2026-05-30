import argparse

"""Begin Phase"""
"""parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display the square of a given number")
if args.verbosity >= 2:
    print(f"{args.x} to the power {args.y} equals to {answer}")
elif args.verbosity >= 1:
    print(f"{args.x}^{args.y} == {answer}")"""



"""-----------------------------------------------------------------------
Advancing -> Positional arguments
--------------------------------------------------------------------------"""
"""parser = argparse.ArgumentParser()
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
    print(answer)"""



"""-----------------------------------------------------------------------
Specifying ambiguous arguments
--------------------------------------------------------------------------"""
"""parser = argparse.ArgumentParser(prog="PROG")
parser.add_argument('-n', nargs="+")
parser.add_argument('args', nargs="*")

# It's ambiguous, so parse_args assumes ita an option
parser.parse_args(['--', '-f'])

# ambiguous so the -n option greedily accepts arguments (consumes them all unless -- 
# is specified to stop the consumption)
parser.parse_args(['-n', '1', '2', '3'])
# (--) specified
parser.parse_args(['-n', '1','--', '2', '3'])"""


"""-----------------------------------------------------------------------
Conflicting Options
--------------------------------------------------------------------------"""
# Introducing **add_mutually_exclusive_group()** -> lets us specify options that
# conflict with each other.
"""parser = argparse.ArgumentParser(description="calculate X to the power of Y")
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
    print(f"{args.x}^{args.y} == {answer}")"""



"""-----------------------------------------------------------------------
CUSTOM TYPE CONVERTERS
--------------------------------------------------------------------------"""
parser = argparse.ArgumentParser(prefix_chars="-+")
