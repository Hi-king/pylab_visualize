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
read csv from stdin and flatten colmn of set to multi columns
=========================================================
''',epilog = '''
=========================================================
hikingko1@gmail.com
2013/8/26
=========================================================
''')

parser.add_argument('columns', type=int, nargs="+")
parser.add_argument('--delimiter', type=str, choices=(",", "t", "n"), default="t")
parser.add_argument('--schema', type=str)

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

    ##===========
    ## process
    ##===========
    inputlines = [line.rstrip().split(delim) for line in sys.stdin]
    itemdict = {column:[] for column in columns}

    for line in inputlines:
        for column in columns:
            item = line[column]
            if not item in itemdict[column]:
                itemdict[column].append(item)
    
    ##=============
    ## output
    ##=============
    ## schema
    if args.schema : 
        schemaline = open(args.schema).readline().rstrip().split(delim)
    else:
        schemaline = ["" for item in inputlines[0]]        
    thisline = []
    for column,value in enumerate(schemaline):
        if column in columns:
            thisline += itemdict[column]
        else:
            thisline.append(value)
    thisline = ["%d: %s"%(column, value) for column, value in enumerate(thisline)]
    print reduce(lambda x,y: str(x)+delim+str(y), thisline)
    
    ## main
    for line in inputlines:
        thisline = []
        for column,value in enumerate(line):
            if column in columns:
                counts = [0 for item in itemdict[column]]
                counts[itemdict[column].index(value)] = 1
                thisline += counts
            else:
                thisline.append(value)
        print reduce(lambda x,y: str(x)+delim+str(y), thisline)
            
 

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
