# BIOL68400 Programming Project
# donatello.py
# By Tengyue Zheng and Seamus Duffy
# 8/11/2017 -10/11/2017

# LRGproject

Task: Pair programming on LRG XML files

Objectives:

Day 1

Explore LRG

Aim: Build a tool to query the LRG database and identify differences between Gr37 and Gr38 for specific genes.

#Question for users

#Q1. What input and output files would you like to query in relation to LRG?
#A1 Gene names, transcript IDs, coordinates (genomic, exon, transcript)

#Q2. What variables do they want to look at from each file?
#A2 LRG genomic coordinates, build37, build38 coordinates

#Q3. What information do we need to compare and contrast between different genes in XML.
#A3 exon start and end, transcript start and end

#4. Create a script that automatically pulls LRG XML files for each genes

#5. Export the information into excel or text file.

#6. Testing of user input, build assert statements to check the output of each function.

Version 1.1

Function:
XML parser for LRGs using Python 3.6.3

To clone Git repository go here: https://github.com/tz2614/LRGproject

LRG data exists in the Git repository or are available from http://ftp.ebi.ac.uk/pub/databases/lrgex/

User Requirements:
-Probe LRG files and pull out relevant information

User Stories:
-Input LRG file
-Input logic tests
-Return gene information including LRG_ID, gene name, genomic coordinates,
	number of transcripts, number of exons and exon locations

Sample Input: donatello.py
"Enter an LRG file:" LRG_343.xml

Sample Output:

LRG_id 		cDNA start		cDNA end 	Strand
GRChBuild	Location 		gDNA start	gDNA end
Gene Sympbol	Chromosome number

Table:
Transcript #	Exon #	Start 	End

#emails
#tony_zheng35@hotmail.com
#duffys11@outlook.com

References

https://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree#id13
