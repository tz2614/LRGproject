import os
import urllib
#import numpy as np
import re

def genename2LRGref(gene):

    genenames = []
    LRGref_list = []
    lines = []

    #open and read LRGref text file
    with open(lrgtext, 'r') as file:
    #create a list of genenames, and a list of LRGrefs

    # iterate over the lines in the lRGref text file
        for line in file:
    # split the line into a list of column values
            if line.startswith("#"):
                pass
            if line.startswith("LRG"):
                lines.append(line)
        pattern = re.compile(r"\bLRG_[0-9]\b")
        print (pattern)
        if pattern.search(line) != None:
            LRGref_list.append(pattern)
        print (pattern)

    print ("gene:", genenames)
    print ("LRGref_list:", LRGref_list)

lrgtext = "list_LRG_GRCh37.txt"
