#!/usr/bin/python
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
Group and count from stream
=========================================================
''',epilog = '''
=========================================================
hikingko1@gmail.com
2013/8/12 ->
=========================================================
''')

parser.add_argument('columns', type=int, nargs="+")
parser.add_argument('--delimiter', type=str, choices=(",", "t", "n"), default="t")

##======##
## main ##
##======##
import math

def main(args):
    def line2key(line, delim, columns):
        linetuple = line.rstrip().split(delim)
        return reduce(lambda x,y:str(x)+delim+str(y), [linetuple[i] for i in columns])

    ##======##
    ## init ##
    ##======##
    columns = args.columns
    delim  = args.delimiter
    if   delim=="t": delim = "\t"
    elif delim=="n": delim = "\n" 

    data = {}
    for line in sys.stdin:
        key = line2key(line, delim, columns)
        data[key] = data[key]+1 if data.get(key) else 1
    #print data
    
    for key,value in data.items():
        print(key+delim+str(value))
    

    


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
