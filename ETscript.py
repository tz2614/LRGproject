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

tree = ET.ElementTree(file='LRG_343.xml')
root = tree.getroot()

for elem in tree.iter(tag='id'):
    print (elem.tag, elem.text)

for elem in tree.iter(tag='lrg_locus'):
    print (elem.tag, elem.text)

for exon in root.iter('exon'):
	label = exon.get('label')
	start = exon[0].get('start')
	end = exon[0].get ('end')
	strand = exon[0].get ('strand')
	if label == None:
		break
	print("exon", label, "start", start, "end", end, "strand", strand)

	








