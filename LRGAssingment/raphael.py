# BIOL68400 Programming Project
# By Tony and Seamy
# 8/11/2017


#How to use it: 1. python donatello.py
#               2. enter filename in following format LRG_XX.xml

#importing packages
import xml.etree.ElementTree as ET
import glob
import os

#user to specify LRG. ?How to make .xml extension automatic?
filename = input('Enter an LRG file e.g LRG_X.xml:')
# check correct xml file is entered
assert filename.endswith ('.xml'), "File should end with the extension .xml"
assert filename.startswith ('LRG_'), "File should start with LRG_.xml"

def xml_info(filename): #determine XML structure
    tree = ET.parse(filename)
    root = tree.getroot()
    UA = tree.getroot()[1]

    return(root, UA)

def gene_info(root): #grab info on genes

    for FA in root.findall("./fixed_annotation"):
        lrg_id = FA.find('id').text

        for transcript in root.findall("./fixed_annotation/transcript"):
            transcript = transcript.get('name')

            path = "./fixed_annotation/transcript/coordinates"
            for coordinates in root.findall(path):
                coord = coordinates.get('coord_system')
                start = coordinates.get('start')
                end = coordinates.get('end')
                strand = coordinates.get('strand')
                int_start = int(start)
                int_end = int(end)
                assert (int_start < int_end), "Genomic start should be smaller than genomic end"


    return (lrg_id, transcript, coord, start, end, strand)

def build_info(UA):

    for child in UA[1].findall('./mapping'):
        chr = child.get('other_name')
        build37 = child.get('coord_system')
        NC_num37 = child.get('other_id')
        gstart37 = child.get('other_start')
        gend37 = child.get('other_end')

        return (chr, build37, NC_num37, gstart37, gend37)

def build_info2(UA):

    for child in UA[1].findall(".//mapping[2]"):
        build38 = child.get('coord_system')
        NC_num38 = child.get('other_id')
        gstart38 = child.get('other_start')
        gend38 = child.get('other_end')

        return (build38, NC_num38, gstart38, gend38)


def gene_name(filename):

    gene = root.find('updatable_annotation/annotation_set/lrg_locus').text
    return (gene)

(root, UA) = xml_info(filename)
(lrg_id, transcript, coord, start, end, strand) = gene_info(root)
(chr, build37, NC_num37, gstart37, gend37) = build_info(UA)
(build38, NC_num38, gstart38, gend38) = build_info2(UA)
(gene) = gene_name(filename)

print (lrg_id, "Transcript:", transcript, "cDNA start:", start, "cDNA end:", end, "strand:", strand)
print (build37,  NC_num37, "Genomic start:", gstart37, "Genomic end:", gend37)
print (build38, NC_num38, "Genomic start:", gstart38, "Genomic end:", gend38)
print('Gene:', gene, "Chr:", chr,)

def get_exon_data(filename):

    transcript_count = 0 #count set to zero
    list_exon_pos= [] #make blank list


    for transcripts in root.findall('./fixed_annotation/transcript'):
        transcript_count += 1 #add 1 to count for every 'transcript' under FA

        exon_lst = root.findall('./fixed_annotation/transcript/exon')
        print( "Transcript number: ", transcript_count, 'Exon count: ', len(exon_lst))


        for exons in transcripts.findall('exon'):
            exon = exons.get('label')

            for coord in exons.findall('coordinates'):

                if (coord.get('coord_system').find("t")!=-1):
                    start_ex = coord.get('start')
                    end_ex = coord.get('end')


            list_exon_pos.append([str(transcript_count), exon, start_ex, end_ex]  )

        print ("T   ",    "Exon     ",     "Start   ",    "End  ")
    for group in list_exon_pos:
        print ("        ".join(group) + "\n")

    return (list_exon_pos)

(list_exon_pos)= get_exon_data(filename)

