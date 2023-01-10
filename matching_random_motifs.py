# Matching Random Motifs

from numpy import random

N = 90284
DNA = 'TTGGCGTTGT'
DNA_len = len(DNA)
GC = 0.514780

G_count = 0
C_count = 0
A_count = 0
T_count = 0 


for base in DNA:

    if base == 'G':
        G_count += 1

    elif base == 'C':
        C_count += 1

    elif base == 'A':
        A_count += 1
    
    elif base == 'T':
        T_count += 1

g_prob = GC/2
c_prob = GC/2
a_prob = (1-GC)/2
t_prob = (1-GC)/2

probability = (g_prob**G_count)*(c_prob**C_count)*(a_prob**A_count)*(t_prob**T_count)

print('probability that GC content will generate DNA: ', probability)

P_not_DNA = 1-probability
P_not_DNA_inlistN = P_not_DNA**N
P_DNA_inlistN = 1- P_not_DNA_inlistN

print('probability that DNA is in list of N kmers with GC content: ', P_DNA_inlistN)