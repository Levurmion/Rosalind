# Independent Alleles

import numpy as np
from math import factorial

# Starts with heterozygous mating Aa Bb * Aa Bb in the 0th generation, makes 2 children
# Children's genotypes will be dependent on their probabilities based on the two parental genotypes
# Every child will always mate with heterozygous individuals (Aa Bb)

# With each generation k, the generation's population grows by 2**k
# k = 0, 2**0 = 1
# k = 1, 2**1 = 2
# k = 2, 2**2 = 4
# k = 3, 2**3 = 8
# ...

# probability of giving Aa Bb offspring from Aa Bb * Aa Bb mating
P_het = 9/16

# probability of giving NOT Aa Bb offspring from Aa Bb mating
P_not_het = 1-P_het

# probability of giving Aa Bb offspring from

print('P(AaBb): ', P_het)
print('P(not AaBb): ', P_not_het)

# However, the probabilities evolve as with each k generation, there will be non-heterozygous individuals that will alter the k+1 generation's probability of getting a heterozygous individual. Find the expected proportion of heterozygous individuals with each generation.

k = 6   # at k-th generation
N = 19   # at least N heterozygous individuals belong to k-th generation


def generation(k,gen=0,P_het=1,P_not_het=0):

    P_het_hetoffspring = 0.5625
    P_not_het_hetoffspring = 0.25

    if gen == k:
        return P_het
    
    else:
        P_het_next = (P_het * P_het_hetoffspring) + (P_not_het * P_not_het_hetoffspring)
        P_not_het_next = 1 - P_het_next
        gen += 1
        return generation(k,gen,P_het_next,P_not_het_next)


def probability(k,N,P_het):

    population_size = 2**k

    P_not_het = 1-P_het

    print(P_not_het)

    prob_to_check = np.arange(N,population_size+1)
    
    P_atleast_N_het = 0

    for p in prob_to_check:

        q = population_size-p
        combinations = factorial(population_size)/(factorial(p)*factorial(q))

        print('combiantions: ', combinations)
        print('p: ', p)
        print('q: ', q)

        P_atleast_N_het += combinations*(P_het**p)*(P_not_het**q)

    print(P_atleast_N_het)


probability(k,N,0.25)

