# Transistions and Transversions

'''
Due to the nature of DNA base chemistry, some DNA point mutations are more common than others. Mutations swapping a purine (A <--> G) or pyrimidine (C <--> T) base with another one of the same type are called TRANSITIONS. In contrast, mutations involving the replacement of a purine base with a pyrimidine or vice versa (A/G <--> C/T) are called TRANSVERSIONS. The latter is much less common because this involves changing the principal structure of the nucleobase (the pyrimidine/purine rings).

For instance, a C --> T transition can easily occur via the action of an endogenous enzyme known as cytidine deaminase. Cytidine deaminase oxidizes the C4 amine group of cytosine into a carbonyl which turns it into uracil (U) - the RNA nucleobase equivalent of T. If the G-U mismatch could not be repaired prior to the next cycle of DNA replication, an A is instead incorporated to basepair with the mutated strand carrying the U in this position. Consequently, the daughter strands of this mutant would exhibit an A-T instead of a G-C pair.

Transversions on the other hand, require much more serious damage in order to occur in DNA. The transition-to-transversion ratio between two strands of non-identical DNA, s1 and s2, can be denoted by R(s1,s2). R(s1,s2) is a useful statistic to predict the potential coding regions of DNA. Non-coding regions typically exhibit R(s1,s2) of about 2 while this often exceeds 3 within coding regions as base transitions are less likely to change the encoded amino acid of a protein especially if it occurs at the wobble position (3rd codon base). Feel free to verify this using the amino acid codon table.

In this example, given two non-identical DNA strings of the same length s1 and s2, calculate their R(s1,s2).
'''

from Bio import SeqIO

file = SeqIO.parse('rosalind_tran.txt','fasta')

SEQUENCES = []

for record in file:
    SEQUENCES.append(str(record.seq))

SEQ_LEN = len(SEQUENCES[0])

transitions = 0
transversions = 0

PYRIMIDINE = set(('C','T'))
PURINE = set(('A','G'))

for i in range(0,SEQ_LEN):

    seq1_base = set(SEQUENCES[0][i])
    seq2_base = set(SEQUENCES[1][i])
    is_purine = (seq1_base.union(seq2_base)).issubset(PURINE)
    is_pyrimidine = (seq1_base.union(seq2_base)).issubset(PYRIMIDINE)

    if seq1_base == seq2_base:
        pass

    elif seq1_base != seq2_base:

        if (is_purine == True) or (is_pyrimidine == True):
            transitions += 1
        
        else:
            transversions += 1

print('transitions: ',transitions)
print('transversions: ',transversions)

print('R(s1,s2): ',transitions/transversions)
