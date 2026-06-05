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


def command(name):
    def decorator(func):
        cmd = subparsers.add_parser(name)
        func(cmd)
        return func
    
    return decorator


@command('hello')
def hello(cmd):
    cmd.add_argument("names", nargs="+")   # take one or more
    
    def run(args):
        print("hello", ",".join(args.names))
    
    cmd.set_defaults(func=run) 


args = parser.parse_args()
args.func(args)


