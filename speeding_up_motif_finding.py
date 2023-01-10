# SPEEDING UP MOTIF FINDING

'''
A naive word search employs the sliding window technique which repeatedly forces comparisons of characters to the beginning of the word whilst incrementing the comparison start index by +1 in the larger query string with every mismatch. The process is repeated until a full match of the query is found within the larger string. This gives a worst-case time complexity of O(n*(n-m)) where n is the length of the word and m is the length of the query.

The Knutt-Moris-Pratt (KMP) algorithm introduces a more efficient approach to string matching by using a "failure function" that compiles repeated substring patterns within each word. This allows the algorithm to systematically skip start indices in the query where full matches are obviously impossible.

A failure function for a word (W) of length n is an array P of length n where each index (P[k]) indicates the length of the longest prefix (W[0:j]) that matches with a suffix ending at index k (W[i:k]). To calculate the failure function, we employ 3 pointers - i, j, and k.

i = keeps track of the start index of the latest suffix that matches with a prefix (is reset to i = k whenever a mismatch occurs with a candidate suffix)
j = keeps track of the end index of the prefix matching to the suffix
k = keeps track of the index being queried in the word to calculate P[k]
'''

from Bio import SeqIO

file = list(SeqIO.parse('rosalind_kmp.txt','fasta'))

W = str(file[0].seq)

word_length = len(W)

P = [0]*word_length


# initialize pointers
i = 1
j = 0
k = 1
counter = 0

# start search
while k < word_length:

    if W[k] != W[j]:

        # print('i: ',i,'k: ',k,'j: ',j)

        new_start_pos_found = False

        while j > 0:
            i += 1
            j -= 1

            # print('adding i to ... :', i)
            # print('deducting j to ... : ', j)
            # print(W[i:k+1])
            # print(W[0:j+1])
            
            if W[i:k+1] == W[0:j+1]:
                new_start_pos_found = True
                j += 1
                break

            else:
                pass
        
        P[k] = j
        k += 1

        if new_start_pos_found == False:
            i = k
        

    elif W[k] == W[j]:

        # print('i: ',i,'k: ',k,'j: ',j, 'match')
        
        P[k] = j+1
        j += 1
        k += 1

        

for p in P:
    print(p,end = ' ')




