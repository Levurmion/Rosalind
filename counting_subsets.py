# COUNTING SUBSETS

'''
Sets are mathematical objects that contain an unordered collection of items. Thus a set A = {1,2,3} is identical to another set B = {1,3,2}. Unlike lists or arrays, sets are not allowed to have duplicate items. Therefore, {1,2,2,3} is not a set.

A set is defined as a subset of another set if all of its elements are found in the other set. In addition, the empty set Ø = {} is by default a subset of every set.

In this excercise, given a positive integer n, calculate the number of possible subsets belonging to the set A = {1,2,3,...,n}.
'''

from math import comb

n = 985
subsets = 0

for k in range(0,n+1):
    subsets = (subsets + comb(n,k))%1000000

print(subsets)