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

'''ext = ".xml"
if filename.endswith ('.xml'):
    valid = TRUE
else:
    print ("please enter a valid file type")
    exit()
###file = './LRGs/LRG_343.xml'#'''

def xml_info(file): #determine XML structure
    tree = ET.parse(filename)
    root = tree.getroot()
    UA = tree.getroot()[1]
    FA = tree.getroot()[0]

    return(root, UA, FA)

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

    return (lrg_id, transcript, coord, start, end, strand)

def build_info(UA):

    for child in UA[1].findall('./mapping/neighbor'):
        chr = child.get('other_name')
        build37 = child.get('coord_system')
        NC_num37 = child.get('other_id')
        gstart37 = child.get('other_start')
        gend37 = child.get('other_end')
        build38 = child.get('other_end')

    return (chr, build37, NC_num37, gstart37, gend37, build38)
"""
    for child in UA[1].findall("./mapping"):    ####how to read second child with same name?
        build38 = child.get('coord_system')
        NC_num38 = child.get('other_id')
        gstart38 = child.get('other_start')
        gend38 = child.get('other_end')
"""


def gene_name(filename):

    gene = root.find('updatable_annotation/annotation_set/lrg_locus').text
    return (gene)

(root, UA, FA) = xml_info(filename)
(lrg_id, transcript, coord, start, end, strand) = gene_info(root)
(chr, build37, NC_num37, gstart37, gend37, build38) = build_info(UA)
(gene) = gene_name(filename)

print (lrg_id, "Transcript:", transcript, "cDNA start:", start, "cDNA end:", end, "strand:", strand)
print (build37,  NC_num37, "Genomic start:", gstart37, "Genomic end:", gend37)
print (build38)
print('Gene:', gene, "Chr:", chr,)

def get_exon_data(filename):

    transcript_count = 0 #transcript count set to zero
    trans_exon_pos= [] #make blank list of exon pos


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

            trans_exon_pos.append([str(transcript_count), exon, start_ex, end_ex]  )

        print ("T   ",    "Exon   ",     "Start   ",    "End   ")
    for group in trans_exon_pos:
        print ("        ".join(group) + "\n")

    return (trans_exon_pos)

(trans_exon_pos)= get_exon_data(filename)



def get_protein_data(filename):

    protein_count = 0 # protein count set to zero
    prot_exon_pos = [] # make  blank list of protein pos

    for proteins in root.findall('./fixed_annotation/transcript'):
        protein_count += 1 #add 1 to count for every protein 'transcript' under FA

        prot_exon_lst = root.findall('./fixed_annotation/transcript/exon')
        print( "protein number: ", protein_count, 'protein exon count: ', len(exon_lst))

        for exons in proteins.findall('exon'):
            exon = exons.get('label')

            for oord in exons.findall('coordinates'):

                if (coord.get('coord_system').find("p")!=-1):
                    start_ex = coord.get('start')
                    end_ex = coord.get('end')

            prot_exon_pos.append([str(protein_count), exon, start_ex, end_ex])

        print ("P   ", "Exon  ", "Start   ", "End   ")
    for group in prot_exon_pos:
        print ("        ".join(group) + "\n")

    return (prot_exon_pos)

(trans_exon_pos)= get_exon_data(filename)



"""
    try:
        prot_block = item.find("sequence")
        protein_seq = prot_block.text
        #print protein_seq
        prot_transcript = item.attrib['name']
        #print transcript
    except:
        print "No protein sequence was found"
    protexons = []
    #print 'for exon in...'
    for exon_item in root.findall(exon_level):
        for exon in exon_item.iter('exon'):
            #print 'for coord in exon'
            for coordinates in exon:
                #print 'if...'
                if coordinates.attrib['coord_system'][-2:] == prot_transcript:
                    start_index = int(coordinates.attrib['start'])
                    end_index = int(coordinates.attrib['end'])
                    assert start_index >= 0, "Exon index out of bounds"
                    assert end_index <= len(protein_seq), "Exon index out of bounds"
                    seq = protein_seq[start_index-1:end_index]
                    protexons.append((exon.attrib['label'], start_index, end_index,seq))
    proteindict[prot_transcript] = protexons
return proteindict
"""

