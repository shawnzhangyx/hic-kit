## This will take a juice format matrix and convert into Dixon format. 
######

import sys
import numpy 

def main(argv): 
  inputfile = argv[1]
  outputfile = argv[2]
  print(inputfile)
  with open(inputfile) as fopen: 
    distance_min = 1e9
    for line in fopen:
      anchor1,anchor2 = line.strip().split()[0:2]
      distance = int(anchor2)-int(anchor1)
      if distance < distance_min:
        distance_min = distance
    chr_max = int(anchor2)
    ngrid = chr_max/distance_min+1    
    print(distance_min,chr_max,ngrid)
    array = numpy.zeros(shape=(ngrid,ngrid))
    fopen.seek(0)
    for line in fopen: 
      anchor1,anchor2,freq = line.strip().split()[0:3]
      idx1 = int(anchor1)/distance_min
      idx2 = int(anchor2)/distance_min
      if freq != "NaN":
        freq = float(freq) 
      else: 
        freq = 0 
      array[idx1,idx2] = array[idx2,idx1] = freq 
#    print(sum(array))
    numpy.savetxt(outputfile,array,fmt="%10.5f",delimiter="\t")

if __name__ == "__main__":
  if len(sys.argv) < 3: 
    usage= "usage: python %s input_filename output_filename"%sys.argv[0]
    print(usage)
    exit(1)
  else: 
    main(sys.argv)
