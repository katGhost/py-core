import argparse
from typing import Optional

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

- Allows you to specify custom typer converters for your command line arguments
- xmpl: Handling arguments with different prefixes and process them accordingly
--------------------------------------------------------------------------"""
"""parser = argparse.ArgumentParser(prefix_chars="-+")

parser.add_argument('-a', metavar='<value>', action='append', type=lambda x: ('-', x))
parser.add_argument('+a', metavar='<value>', action='append', type=lambda x: ('+', x))

args = parser.parse_args()
print(args)"""




"""-----------------------------------------------------------------------
USING DECORATORS TO DECLARE A COMMAND RUNNER

- Allows us to define a command/commands for the arguments, cleaner than ->
- repetitively using parser.add_argument()
- 
--------------------------------------------------------------------------"""
# Create a command decorator
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(required=True)   # require/allow subparsers


def command(name: Optional[str] = None):
    def decorator(func):
        cmd = subparsers.add_parser(name)
        cmd.set_defaults(func=func)
        return cmd
    
    return decorator


@command()
def hello(args):
    print('Hello')


args = parser.parse_args()
args.func(args)




# if __name__ == '__main__':
