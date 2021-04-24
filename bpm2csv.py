import pandas as pd
import numpy as np
import glob, os, re

def bpm2csv(fname):
    """ function converting bpm file to 2 csv files for M and v histograms """
    data = [[], []] # double array for data collection 
    d_driven = 0    # vars 

            
    with open(fname, 'r', encoding="iso8859_2") as f:
            f.readline()    # skip first line

            # read the torque histogram
            while True:
                    line = f.readline()
                    if line == "\n":
                            break
                    # print(line)

                    x = int(line[:6])
                    y = int(line[6:])

                    data[0].append([x,y])

            f.readline() # skip second title line

            # read the speed histogram
            while True:    
                    line = f.readline()
                    if line == "\n":
                            break
                    
                    x = int(line[:6])
                    y = int(line[6:])

                    data[1].append([x,y])
            
            line = f.readline() # last line with distance driven

            # regex search for distance driven
            p = re.compile('[0-9]+')
            d_driven = int(p.search(line).group())
            
            # print(data)

    # convert to csv
    df = pd.DataFrame(data[0], columns =['M', "occurence"])
    df.M = np.linspace(-500, 500, 40)

    df2 = pd.DataFrame(data[1], columns =['v', "occurence"])
    df2.v = np.linspace(0, 100, 40)

    # filename
    fname = fname.split('.')[0]

    df.to_csv(fname + "_M.csv")
    df2.to_csv(fname + "_v.csv")

import argparse
parser = argparse.ArgumentParser(description=".bpm file to csv converter. "
        "Currently setup for given format of files, no warranties ;)")
parser.add_argument("fname", nargs='*', help="bpm files selected for conversion", default=None)
parser.add_argument("-a", "--all", action="store_true", help="Convert all .bpm "
		"files present in the directory")
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()

if args.all:
    fnames = glob.glob('*.bpm')
    for fname in fnames:
        try:
            bpm2csv(fname)
            if args.verbose:
                print("{}: converted".format(fname))
        except:
            if args.verbose:
                print("{}: could not convert".format(fname))
elif args.fname is not None:
    for fname in args.fname:
        try:
            bpm2csv(fname)
            if args.verbose:
                print("{}: converted".format(fname))
        except:
            if args.verbose:
                print("{}: could not convert".format(fname))

