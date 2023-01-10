# DISTANCE MATRICES

'''
The construction of phylogeny trees often rely on the initial deduction of pairwise evolutionary distances between different taxa compiled in a distance matrix. In this example, we will create a distance matrix based of the Hamming distance between pairs of taxa. We normalize these metrics into a p-distance (dp).

Where for two strings (s1 and s2) of the same length, dp is given by:

dp(s1,s2) = (Hamming distance between s1 and s2)/(length of s1 or s2)
'''

from Bio import SeqIO
import numpy as np


# Hamming distance
def hamm_dist(string1,string2):

    string_len = len(string1)

    hamm_distance = 0

    for i in range(0,string_len):
        
        if string1[i] == string2[i]:
            pass
        elif string1[i] != string2[i]:
            hamm_distance += 1
    
    return hamm_distance



file = list(SeqIO.parse('rosalind_pdst.txt','fasta'))

TAXA = []

for record in file:
    TAXA.append(str(record.seq))

num_taxa = len(TAXA)
taxa_len = len(TAXA[0])

# initialize a num_taxa x num_taxa matrix
distance_matrix = np.zeros((num_taxa,num_taxa))

# fill in distance_matrix with Hammind distances between each taxonomic pair
for i in range(0,num_taxa):
    for j in range(0,num_taxa):
        distance_matrix[i,j] = hamm_dist(TAXA[i],TAXA[j])

# divide the entire matrix by the length of each taxa
distance_matrix /= taxa_len

print(distance_matrix)


# print output
for i in range(0,num_taxa):
    print('\n')
    for j in range(0,num_taxa):
        print(distance_matrix[i,j],end=' ')