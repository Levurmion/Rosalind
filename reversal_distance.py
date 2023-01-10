# REVERSAL DISTANCE

'''
The most common type of genome rearrangement is an inversion whereby two synteny blocks exchange places on the chromosome, inverting the sequence of their occurence in the chromosome. A reversal occurs when two elements in a permutation exchange places. For example, [5,2,3,4,1] is a reversal of [5,3,2,4,1]. The reversal distance (drev) between two permutations is the minimum number of reversals required to transform one permutation to another.

In this exercise, given pairs of permutations all of which have length = 10, calculate the reversal distance between the two.
'''

from itertools import permutations
import numpy as np
from collections import defaultdict

def hamm_dist(l1,l2):

    hamm = 0

    for i in range(0,len(l1)):
        if l1[i] != l2[i]:
            hamm += 1
        else:
            pass

    return hamm


def invert_permutation(perm,index1,index2):
    
    item1 = perm[index1]
    item2 = perm[index2]

    inv_perm = list.copy(perm)
    inv_perm[index1] = item2
    inv_perm[index2] = item1

    return inv_perm


def remove_matched(perm1,perm2):

    matched = []

    for i in range(0,len(perm1)):
        if perm1[i] == perm2[i]:
            matched.append(perm2[i])
    
    for match in matched:
        perm2.remove(match)
        perm1.remove(match)

    return perm1, perm2


def reversal_distance(perm1,perm2,count=0,discovered_paths=[]):

    this_perm1 = list.copy(perm1)
    this_perm2 = list.copy(perm2)

    this_perm1, this_perm2 = remove_matched(this_perm1,this_perm2)

    print(this_perm1,this_perm2)

    # if both arrays empty, all items matched so take in as a discovered path
    if this_perm1 == [] and this_perm2 == []:
        print('path discovered: ',count)
        print()
        discovered_paths.append(count)

    # accept change if the inversion resulted in a new match and continue recursion
    if (len(this_perm2) < len(perm2)) or (count == 0):
        count += 1

        for i in range(0,len(this_perm2)):
            for j in range(1,len(this_perm2)):
                inv_perm2 = invert_permutation(this_perm2,i,j)
                print('this perm 1:    ',this_perm1)
                print('this perm 2:    ',this_perm2)
                print('inverted perm2: ',inv_perm2)
                print()
                reversal_distance(this_perm1,inv_perm2,count,discovered_paths)
        
        return min(discovered_paths)

    # reject change if the inversion resulted in no new matches and terminate the recursion branch
    elif len(this_perm2) == len(perm2):
        return


print(reversal_distance([3, 10, 8, 2, 5, 7, 1],[5, 2, 3, 1, 7, 10, 8]))