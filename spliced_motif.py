# Finding a Spliced Motif

'''
A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

As a substring can have multiple locations, a subsequence can have multiple collections of indices, and the same index can be reused in more than one appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT in 8 different ways.
'''

from Bio import SeqIO

file = list(SeqIO.parse('rosalind_sseq.txt','fasta'))

DNA_STRING = str(file[0].seq)
MOTIF = str(file[1].seq)

i = 0
j = 0

indices = []

while i < len(DNA_STRING) and j < len(MOTIF):

    if DNA_STRING[i] != MOTIF[j]:
        i += 1
    elif DNA_STRING[i] == MOTIF[j]:
        indices.append(i+1)
        i += 1
        j += 1

for index in indices:
    print(index,end=' ')
