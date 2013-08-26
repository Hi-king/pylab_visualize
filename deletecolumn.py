#!/usr/bin/python
# -*- coding: utf-8 -*- 

##==========##
## argument ##
##==========##
import argparse
import sys
class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

class MyFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter): pass            
parser = ArgumentParser(
formatter_class=MyFormatter,
description='''
=========================================================
delete specific column
=========================================================
''',epilog = '''
=========================================================
hikingko1@gmail.com
2013/8/26
=========================================================
''')

parser.add_argument('columns', type=int, nargs="+")
parser.add_argument('--delimiter', type=str, choices=(",", "t", "n"), default="t")

##======##
## main ##
##======##
def main(args):
    ##======##
    ## init ##
    ##======##
    columns = args.columns
    delim = args.delimiter
    if   delim=="t": delim = "\t"
    elif delim=="n": delim = "\n"

    ##=============
    ## output
    ##=============
    for line in sys.stdin:
        splittedline = line.rstrip().split(delim)
        thisline = []
        for column,value in enumerate(splittedline):
            if not column in columns:
                thisline.append(value)
        print reduce(lambda x,y: str(x)+delim+str(y), thisline)

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
