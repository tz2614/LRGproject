#!/usr/bin/python
"""
from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("LRG_214.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print "Root element : %s" % collection.getAttribute("shelf")

# Get all the movies in the collection
movies = collection.getElementsByTagName("movie")

# Print detail of each movie.
for movie in movies:
   print "*****Movie*****"
   if movie.hasAttribute("title"):
      print "Title: %s" % movie.getAttribute("title")

   type = movie.getElementsByTagName('type')[0]
   print "Type: %s" % type.childNodes[0].data
   format = movie.getElementsByTagName('format')[0]
   print "Format: %s" % format.childNodes[0].data
   rating = movie.getElementsByTagName('rating')[0]
   print "Rating: %s" % rating.childNodes[0].data
   description = movie.getElementsByTagName('description')[0]
   print "Description: %s" % description.childNodes[0].data
"""

import urllib2
#import xmltodict
#import xml.etree.ElementTree as ET
response = urllib2.urlopen('http://www.lrg-sequence.org/downloads')

print "The URL is: ", response/geturl()
def homepage(request):
    file = urllib2.urlopen('http://www.lrg-sequence.org/downloads')
    data = file.read()
    file.close()

    data = xmltodict.parse(data)
    return render_to_response('my_template.html', {'data': data})
"""
