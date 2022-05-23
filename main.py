import sys
import getopt
import os
from termcolor import colored

from src.main import test

os.system('color')

def _usage():
    cmd = 'clear'
    if os.name in ('nt', 'dos'):
        cmd = 'cls'

    os.system(cmd)

    print("\
-h   --help     Prints this information\r\n\
-s   --start    Starts the bot with a provided config.json file"
)
        

if __name__ == "__main__":
    argumentList = sys.argv[1:]
    options = "hs"
    l_options = ["help", "start"]

    try:
        args, values = getopt.getopt(argumentList, options, l_options)

        if len(args) <= 0:
            raise
    except:
        _usage()
        sys.exit(2)

    for curArg, curValue in args:

        if curArg in ("-h", "--help"):
            _usage()
            sys.exit(2)

        elif curArg in ("-s", "--start"):
            test.go()

        else:
            _usage()
            sys.exit(2)