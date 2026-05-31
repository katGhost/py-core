import argparse

"""-----------------------------------------------------------------------
Specifying ambiguous arguments
--------------------------------------------------------------------------"""
parser = argparse.ArgumentParser(prog="PROG")
parser.add_argument('-n', nargs="+")
parser.add_argument('args', nargs="*")

# It's ambiguous, so parse_args assumes ita an option
parser.parse_args(['--', '-f'])

# ambiguous so the -n option greedily accepts arguments (consumes them all unless -- 
# is specified to stop the consumption)
parser.parse_args(['-n', '1', '2', '3'])
# (--) specified
parser.parse_args(['-n', '1','--', '2', '3'])