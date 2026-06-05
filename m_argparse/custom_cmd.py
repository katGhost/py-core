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
subparsers = parser.add_subparsers(required=True, dest="command")   # require/allow subparsers

arguments = [
    {
        "flags": ["square"],
        "kwargs": {
            "type": int,
            "help": "display the square of a given number"
        }
    },
    {   "flags": ["names"],
        "kwargs": {
            "type": str,
            "help": "display the names(s) specified in the args"
        }
    },
    {
        "flags": ["-v", "--verbosity"],
        "kwargs": {
            "type": int,
            "help": "increase the output verbosity"
        }
    },
]


def command(name):
    def decorator(func):
        cmd = subparsers.add_parser(name)
        
        for arg in arguments:
            cmd.add_argument(*arg["flags"], **arg["kwargs"])
        
        cmd.set_defaults(func=func)  # attach handler
        return func

    return decorator


@command("custom")
def custom(args):
    
    
    if args.verbosity is None:
        print(args.square **2)
        print(args.names)
    else:
        print(f"{args}^ to the  args.square **2")
        print(args.names)
        


args = parser.parse_args()
args.func(args)


