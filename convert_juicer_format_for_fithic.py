#!/usr/bin/python

#########################################
# Author: Yunjiang Qiu <serein927@gmail.com>
# File: interaction2bin.py
# Create Date: 2015-03-22 13:46:10
#########################################

import operator
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='sum bin for fit hic')
    parser.add_argument("-i", "--interaction", dest="interaction",required=True,help="interaction file")
    parser.add_argument("-b", "--bias", dest="bias",required=True,help="bias file")
    parser.add_argument("-o", "--out", dest="outfile",required=True,help="output file")
    args = parser.parse_args()

    interaction_map = {}
    with open(args.interaction, 'r') as f:
        for line in f:
            chr1,start,chr2,end,count = line.rstrip().split('\t')
            key1 = '\t'.join([chr1,start])
            key2 = '\t'.join([chr2,end])
            try:
                interaction_map[key1] += int(count)
            except KeyError:
                interaction_map[key1] = int(count)
            try:
                interaction_map[key2] += int(count)
            except KeyError:
                interaction_map[key2] = int(count)

    with open(args.outfile, 'w') as fo:
        with open(args.bias, 'r') as f:
            for line in f:
                [chr,bin,bias] = line.rstrip().split('\t')

                if bias == "1.0":
                    map = 0
                else:
                    map = 1
            
                try:
                    tmp = [chr,0,bin,interaction_map['\t'.join([chr,bin])],map]
                except KeyError:
                    tmp = [chr,0,bin,0,map]
                
                fo.write("%s\n" % '\t'.join([str(x) for x in tmp]))

if __name__ == "__main__":
    sys.exit(main())
