############################
## This script will find all the matepairs anchoring in a certain 
## genomic region. There are two output files: 
## POS 1: the read position within the genomic region
## POS 2: the read mapping to alternative region. 
## ######################### 

import sys
import pysam

def main(argv):
  filename = argv[1]# "D0_HiC_Rep1.bam" #argv[1]
  chr = argv[2] #"chr14" #argv[2]
  start = int(argv[3]) #23866000 # argv[3]
  end = int(argv[4]) #23882000 # argv[4]
  outdir = argv[5]
  sam = pysam.Samfile(filename,'rb')
  fread_list = []
  rread_list = []
  num = 0
  for read in sam.fetch(reference=chr,start=start,end=end):
    num += 1
    if num % 100 == 0:
      print num, "lines processed"
    fread_list.append(read.pos)
    rread_list.append(sam.mate(read).pos)
  outf1 = open(outdir+filename+'_pos1.txt','w')
  for pos in fread_list:
    outf1.write(str(pos)+'\n')
  outf2 = open(outdir+filename+'_pos2.txt','w')
  for pos in rread_list:
    outf2.write(str(pos)+'\n')


if __name__ == "__main__":
  main(sys.argv)

