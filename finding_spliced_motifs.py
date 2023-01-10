# FINDING A SPLICED MOTIF

'''
Given that the coding regions of eukaryotic genes are often interspersed by introns, the motifs shared by two genes do not necessarily have to be contiguous. Thus, finding common motifs between genes often present themselves as common subsequence/substring problems which can be solved via dynamic programming.

In this example, given two DNA strings, find the longest common subsequence between them.

DYNAMIC PROGRAMMING using Needleman-Wunsch Algorithm
'''

import numpy as np
from Bio import SeqIO

def longest_subsequence(string1,string2):

    longest_subseq = ''

    print('string 1: ', string1)
    print('string 2: ', string2)

    row = len(string1)
    col = len(string2)

    align_matrix = np.zeros((row+1,col+1))
    path_matrix = np.zeros((row+1,col+1))

    # fill in alignment matrix
    for i in range(1,row+1):

        for j in range(1,col+1):

            if string1[i-1] == string2[j-1]:
                align_matrix[i,j] = align_matrix[i-1,j-1] + 1
                path_matrix[i,j] = 1
            
            else:
                top_and_left = [align_matrix[i-1,j],align_matrix[i,j-1]]
                max_value = max(top_and_left)
                align_matrix[i,j] = max_value
                    
                if (top_and_left[0] == top_and_left[1]) or (top_and_left[0] > top_and_left[1]):
                    path_matrix[i,j] = 2
                    
                elif top_and_left[0] < top_and_left[1]:
                    path_matrix[i,j] = 3

    # print('alignment matrix: \n',align_matrix)
    # print('path matrix: \n', path_matrix)
    
    # traceback through path matrix
    last_row = list(align_matrix[row])
    max_value = np.max(last_row)

    col_counter = last_row.index(max_value)
    row_counter = row

    end = False

    while end == False:

        path = path_matrix[row_counter,col_counter]

        if path == 1:
            longest_subseq = string2[col_counter-1] + longest_subseq
            col_counter -= 1
            row_counter -= 1
        
        elif path == 2:
            row_counter -= 1
        
        elif path == 3:
            col_counter -= 1
        
        elif path == 0:
            end = True

    return longest_subseq
    


file = SeqIO.parse('rosalind_lcsq.txt','fasta')

records = [record for record in file]

dna_1 = records[0].seq
dna_2 = records[1].seq

print('\nlongest subsequence: ', longest_subsequence(dna_1,dna_2))
