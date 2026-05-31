import argparse
from typing import Optional

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


@command('--v')
def hello(args):
    print('Hello')


args = parser.parse_args()
args.func(args)


