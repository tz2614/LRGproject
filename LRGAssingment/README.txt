# BIOL68400 Programming Project
# donatello.py
# By Tony and Seamy
# 8/11/2017 



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
