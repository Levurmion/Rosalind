# Perfect Matchings and RNA Secondary Structure

'''
Because RNA occurs mostly as a single-stranded polymer, it is feasible that two complementary stretches of bases separated by some distance could come together and pair up and force the entire molecule to twist and fold. The 3D shapes formed by this phenomenon are known as the RNA's secondary structures.

RNA folding can be predicted by modelling the bases of a given RNA sequence as the nodes of a graph. The different ways in which the bases could interact intramolecularly can then be modelled by matching the bases (A with U and G with C) across the strand.

A perfect matching can only occur when a graph G has an even number of nodes (2n). If we denote the total number of possible perfect matchings in G as Pn, for a given node x, there are 2n - 1 ways to connect x to the other nodes of the graph. Subsequently, there will be 2n - 3 ways to connect a second (unconnected) node to the remaining nodes. Therefore, Pn can be written as the recurrence relation:

Pn = (2n - 1) * Pn-1 * ... P1

Given that P1 = 1, we can construct a recursive function that calculates Pn with a base case where if n = 1, it returns 1.
'''

import numpy as np

RNA_STRING = 'CUGAUGCCCAGCUUAGUUCGCUCGCCUGUAUCGGAACAGCCAUAUGGAGACAUGCUUAGAGGACCUAAGUCGCUAACUGG'

# count numbers of each base
A = 0
U = 0
G = 0
C = 0

for i in range(0,len(RNA_STRING)):

    if RNA_STRING[i] == 'A':
        A += 1
    elif RNA_STRING[i] == 'U':
        U += 1
    elif RNA_STRING[i] == 'G':
        G += 1
    elif RNA_STRING[i] == 'C':
        C += 1

AU_fac_arr = np.arange(1,A+1,dtype=object)  # dtype=object to tell numpy to use Python's long integer object
GC_fac_arr = np.arange(1,G+1,dtype=object)  # this avoids integer overflows

AU_choices = 1
GC_choices = 1

for num in AU_fac_arr:
    AU_choices = AU_choices * num

for num in GC_fac_arr:
    GC_choices = GC_choices * num

perfect_matchings = AU_choices * GC_choices

print(perfect_matchings)
