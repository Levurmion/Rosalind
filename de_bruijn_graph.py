# DE BRUIJN GRAPH

'''
Given a collection of DNA reads (could be repetitive) corresponding to set of (k+1)-mers, construct an adjacency list of directed edges representing the De Bruijn Graph that can be formed by the library.
'''


# function to find reverse complement
def reverse_comp(string):

    basepairs = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    revc = ''

    for base in string[::-1]:
        revc = revc + basepairs[base]
    
    return revc


# program start
filename = 'rosalind_dbru.txt'

with open(filename,'r') as file:

    READS = file.readlines()
    READS = [read.strip() for read in READS]

revc_reads = []

# generate reverse complements
for read in READS:
    revc_reads.append(reverse_comp(read))

# combine the revc_reads array into the main READS array
READS = READS + revc_reads

# remove redundancies
READS = set(READS)

# initialize a set of non-redundant edges
edges = set()

# generate edge pairs of (read[0:k],read[1:k+1])
for read in READS:

    k = len(read)-1
    edges.add((read[0:k],read[1:k+1]))

# print to output txt file
with open('rosalind_dbru_out.txt', 'w') as outfile:

    for edge in edges:
        outfile.write('('+edge[0]+', '+edge[1]+')'+'\n')

