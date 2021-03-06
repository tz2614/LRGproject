# BIOL68400 Programming Project
# By Tony and Seamy
# 8/11/2017

#Questions
###### do we want to reference a website or a folder for XMLs? (link to XMLs http://ftp.ebi.ac.uk/pub/databases/lrgex)/
###### Pending vs public LRGs

#How to use it: python ETscript.py

#importing packages
import xml.etree.cElementTree as ET
import os
import glob
import sys

#def geneinfoparser(fileName):

#code taken from reference below to check that https://github.com/MattWellie/XML_Parser/blob/master/XML_Parser.py
#fileName = sys.argv[1]
#assert fileName[-4:] == '.xml', 'You have the wrong input file'
#assert len(sys.argv) <4, "Too many arguments!"

def geneinfoparser(xmlfile):
    # raw_input section not working!
    xmlfile = input('Enter file path to your LRG XML file:')
    if not xmlfile:
        print ("no file path entered!")
    else:
        print ("file path entered")

    tree = ET.ElementTree(file=xmlfile)
    root = tree.getroot()

    #Find LRI_ID and append into a list
    LRG_ID = []
    for elem in tree.iter(tag='id'):
        print (elem.tag, elem.text)
        LRG_ID.append(elem.text)
        print (LRG_ID)

    #Find LRI_gene and append into a list
    for elem in tree.iter(tag='lrg_locus'):
        print (elem.tag, elem.text)
        LRG_gene = []
        LRG_gene.append(elem.text)
        print (LRG_gene)

    LRGdict = {}

    #So for each LRG XML, we parse the exon number, start and end of the exon and strand number into a dictionary
    for exon in root.iter('exon'):
        label = exon.get('label')
        start = exon[0].get('start')
        end = exon[0].get ('end')
        strand = exon[0].get ('strand')
        if label == None:
            break
        else:
            LRGdict["exon"] = label
            LRGdict["start"] = start
            LRGdict["end"] = end
            LRGdict['strand'] = strand
    	#print("exon", label, "start", start, "end", end, "strand", strand)
        print (LRGdict)

#LRGdict = { 'gene': 'LRGref',
    #      'exon': 'number',






