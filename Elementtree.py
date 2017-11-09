#!/usr/bin/python

import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='LRG_214.xml')
root = tree.getroot()
#root = ET.fromstring('LRG_214.xml')

print (root.tag, root.attrib)
#for child in root:
    #print (child.tag)
