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

#code taken from reference below to check that (https://github.com/MattWellie/XML_Parser/blob/master/XML_Parser.py)
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

"""
def get_exoncoords(level,padding,genseq):
    '''Traverses the XML eTree to identify all the exons for the sequence
       Returns a dictionary containing exon numbers, start and finish
       co-ordinates, and the appropriate chunk of sequence.
       The dictionary is designed to be passed to a dedicated write function
       which will print the appropriate sequence elements and identifiers to
       an output file'''
    transcriptdict = {} #LRG files can contain more than one transcript in fixed annotation section
    for items in level.findall('transcript'):
        transcript = items.attrib['name']
        tranexons = []
        for exon in items.iter('exon'):
            for coordinates in exon:
                if coordinates.attrib['coord_system'][-2:] == transcript:
                    #ensures only genomic coords are taken
                    startIndex = int(coordinates.attrib['start'])
                    endIndex = int(coordinates.attrib['end'])
                    assert startIndex >= 0, "Exon index out of bounds"
                    assert endIndex <= len(genseq), "Exon index out of bounds"
                    seq = genseq[startIndex-1:endIndex]
                    if padding > 0:
                        assert startIndex - pad >= 0, "Exon index out of bounds"
                        assert endIndex + pad <= len(genseq), "Exon index out of bounds"
                        pad5 = genseq[startIndex-padding-1:startIndex]
                        pad3 = genseq[endIndex:endIndex+padding+1]
                        seq = pad5.lower() + seq + pad3.lower()
                    tranexons.append((exon.attrib['label'],startIndex, endIndex,seq))
                #can add extra elif options to grab other sequence types
        transcriptdict[transcript] = tranexons
return transcriptdict
"""







