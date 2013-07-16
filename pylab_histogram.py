#! /usr/bin/python
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
Visualize Histogram
=========================================================
''',epilog = '''
=========================================================
hikingko1@gmail.com
2013/7/8
=========================================================
''')

parser.add_argument('input_csv', type=str)
parser.add_argument('--column', type=int, default=1)
parser.add_argument('--xlabel', type=str, default="")
parser.add_argument('--ylabel', type=str, default="")
parser.add_argument('--delimiter', type=str, choices=(",", "t", "n"), default=",")

##========##
## Import ##
##========##
import pylab

##===========##
## Functions ##
##===========##
def main(args):
    ##======##
    ## init ##
    ##======##
    targetfile = args.input_csv
    targetcol = args.column
    delim  = args.delimiter
    xlabel = args.xlabel
    ylabel = args.ylabel
    if   delim=="t": delim = "\t"
    elif delim=="n": delim = "\n" 
    
    ##======##
    ## main ##
    ##======##
    counts = [int(line.rstrip().split(delim)[targetcol]) for line in open(targetfile)]
    print counts
    
    plots = [0 for i in xrange(max(counts)+1)]
    for item in counts:
        plots[item] += 1
     
    ##======##
    ## show ##
    ##======##
    pylab.xlabel(unicode(xlabel, sys.stdin.encoding))
    pylab.ylabel(unicode(ylabel, sys.stdin.encoding))
    pylab.bar(range(len(plots)), plots)
    pylab.show()
    

if __name__ == '__main__':
    args = parser.parse_args()
    print args
    main(args)
