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
Visualize Barplot Using 2 Columns
=========================================================
''',epilog = '''
=========================================================
hikingko1@gmail.com
2013/7/30
=========================================================
''')

parser.add_argument('input_tsv', type=str)
parser.add_argument('-s', action="store_true")
parser.add_argument('--xdatacol', type=int, default=0)
parser.add_argument('--ydatacol', type=int, default=1)
parser.add_argument('--xlabel', type=str, default="")
parser.add_argument('--ylabel', type=str, default="")
parser.add_argument('--delimiter', type=str, choices=(",", "t", "n"), default="t")

##========##
## Import ##
##========##
import pylab
import os.path

##===========##
## Functions ##
##===========##
def main(args):
    ##======##
    ## init ##
    ##======##
    targetfile = args.input_tsv
    xdatacol   = args.xdatacol
    ydatacol   = args.ydatacol
    delim      = args.delimiter
    if   delim=="t": delim = "\t"
    elif delim=="n": delim = "\n" 
    xlabel     = args.xlabel
    ylabel     = args.ylabel
    tosave     = args.s
    if tosave: savefilename = os.path.splitext(targetfile)[0] + "_boxplot.png"

    ##===========##
    ## read data ##
    ##===========##
    xitems = list(set([float(line.rstrip().split(delim)[xdatacol]) for line in open(targetfile)]))
    #xitems.append(0.0)
    xitems.sort()
    data = {}
    for item in xitems:
        data[item] = []
    #data[0.0] = [0.0]
    for line in open(targetfile):
        lineitems = line.rstrip().split(delim)
        key, val = float(lineitems[xdatacol]), float(lineitems[ydatacol])
        data[key].append(val)
        
    ##======##
    ## show ##
    ##======##
    fig = pylab.figure()
    pylab.xticks(range(len(xitems)), xitems)
    pylab.xlabel(unicode(xlabel, sys.stdin.encoding))
    pylab.ylabel(unicode(ylabel, sys.stdin.encoding))

    for key in xitems:
        print key, data[key]
    showdata = [ data[key] for key in xitems ]
    pylab.boxplot(showdata)

    maxy = max([max(data[key]) for key in xitems])
    pylab.plot([1.0,len(xitems)], [0, maxy], 'k--')
    if not tosave:
        pylab.show()
    else:
        pylab.savefig(savefilename)


    print data


if __name__ == '__main__':
    args = parser.parse_args()
    print args
    main(args)
