# CATALAN NUMBERS AND RNA PSEDUOKNOTS

'''
Pseudoknots are formed when the bases immediately adjacent to the end of a stem-loop structure crosses over to pair with bases across the stem - causing the molecule to fold over itself. In reality, the RNA secondary structure (bonding of atoms) restricts the formation of pseudoknots. However, they do occur in rare cases in which the nucleotide sequence sufficiently permits the folding energy to exceed the energetic constraints of such conformations. Bio-computational algorithms do not currently have sufficiently accurate models to describe the likelihood of RNA sequences in forming pseudoknots. Therefore, existing programs deliberately forbid the modelling of pseudoknots (considering their rarity) to opt for the more accurate prediction of other RNA tertiary structures.

In a bonding graph, pseudoknots are formed when the edges connecting nodes (bases) intersect. To visualize, for a bonding graph of sequenced nodes:

i-j-k-l

the edges are said to cross-over if the connect [i,k] and [j,l].

However, the following combinations do not cross-over:
[i,j] and [k,l]
[i,l] and [j,k]

A generalisation of this is if i, j, k, and l were assigned integer values from 1 to 4, the bonding graph is said to cross-over when:

However, the solution below utilizes recursion with memoization.
'''

from math import factorial
import timeit

def count_noncross_matchings(string,memo={}):

    # store basepair dictionary
    basepairs = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}

    # check first if the string has an even-number of characters
    if len(string)%2 != 0:
        return 0 # invalid entry

    # base case of empty subtring indicating immediately adjacent or end pairing (no substrings within string[0:m] or after string[m])
    elif string == '':
        return 1 # catalan number 0

    # count numbers of each base in longer substrings
    A = 0
    U = 0
    G = 0
    C = 0

    for i in range(0,len(string)):

        if string[i] == 'A':
            A += 1
        elif string[i] == 'U':
            U += 1
        elif string[i] == 'G':
            G += 1
        elif string[i] == 'C':
            C += 1
    
    # base case if substrings do not have equal frequencies of A=U and G=C
    if (A != U) or (G != C):
        return 0 # invalid substring combination
    
    else:
        subs_length = len(string)
        max_k = subs_length//2

        total_catalan_from_m = 0

        for k in range(1,max_k+1):

            m = 2*k

            if basepairs[string[0]] != string[m-1]:
                pass

            if basepairs[string[0]] == string[m-1]:
                subs_left = string[1:m-1]
                subs_right = string[m:]

                try:
                    catalan_left = memo[subs_left]
                except KeyError:
                    catalan_left = count_noncross_matchings(subs_left)
                    memo[subs_left] = catalan_left

                try:
                    catalan_right = memo[subs_right]
                except KeyError:
                    catalan_right = count_noncross_matchings(subs_right)
                    memo[subs_right] =  catalan_right
                
                catalan_product = catalan_left * catalan_right
                total_catalan_from_m += catalan_product

        return total_catalan_from_m
        


STRING = 'AAGCGCGCUAGCGCGGCCCGGUACUAUUGGUACGUAUUAAGAUCCCGCAAGCUAUAUAUCUAAGCGCGCUGUAUCGUAGCAUGAUCCGAGCCGGCAGCUACCUAGAGCCUGCAGUUAGCACGUGCGCGUAUUACAGCGCCGGCAUAUAUUUAAUUAAUUAUCUAGAGAUUCUGAAUUAAUUAUUUAACAUAAUCCGGAUAUGGGCGCCGCGCUAUGUAGUACCGCCGCCGGAUAUAGCCGUCGAGUACGUAUAUGAUAUAUCUAACGCAGUACUGCGC'

start = timeit.timeit()
total_matchings = count_noncross_matchings(STRING)
stop = timeit.timeit()


print('code runtime: ',stop-start,'s')
print(total_matchings)







    
    


    

    





