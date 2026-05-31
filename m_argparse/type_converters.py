import argparse

"""-----------------------------------------------------------------------
CUSTOM TYPE CONVERTERS

- Allows you to specify custom typer converters for your command line arguments
- xmpl: Handling arguments with different prefixes and process them accordingly
--------------------------------------------------------------------------"""
parser = argparse.ArgumentParser(prefix_chars="-+")

parser.add_argument('-a', metavar='<value>', action='append', type=lambda x: ('-', x))
parser.add_argument('+a', metavar='<value>', action='append', type=lambda x: ('+', x))

args = parser.parse_args()
print(args)

