# Genome Assembly

'''
Current sequencing technologies are limited to sequencing small fragments of a genome called 'reads' which have to be reconstructed in silico. For a collection of strings (in this case DNA sequence reads), a longer string containing all the strings in the collection as its substring is called the 'superstring'. Via the assumption of parsimony, the shortest superstring that can be formed from these reads serves to be the candidate chromosome.

parsimony: The biological principle that nature tends to take the shortest path in evolution.

In this example, given a collection of 50 DNA strings, give the shortest superstring containing all of the provided DNA strings.

*The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
'''

from Bio import SeqIO
import time

file = SeqIO.parse('rosalind_long.txt','fasta')

READS = [str(record.seq) for record in file]
READS_CHECK = list.copy(READS)

superstring = ''

time_start = time.time()

while READS != []:
    
    if superstring == '':
        superstring = READS[0]
        del READS[0]
    
    else:

        for candidate in READS:

            midpoint = len(candidate)//2    # floor division to return an integer in case of odd-number lengths

            left_half = candidate[:midpoint]
            right_half = candidate[midpoint:]

            left_half_idx = superstring.find(left_half)     # Python string method to find the lowest index of the query substring if found in the superstring
            right_half_idx = superstring.find(right_half)   # .find() method returns -1 if substring is not found in the superstring

            if left_half_idx != -1:
                rem_superstring = superstring[left_half_idx+len(left_half):]

                if rem_superstring == right_half[0:len(rem_superstring)]:
                    superstring = superstring + right_half[len(rem_superstring):]
                    READS.remove(candidate)
                
                else:
                    pass
            
            elif right_half_idx != -1:
                rem_superstring = superstring[:right_half_idx]

                if rem_superstring in left_half[len(left_half)-len(rem_superstring):]:
                    superstring = left_half[:len(left_half)-len(rem_superstring)] + superstring
                    READS.remove(candidate)
                
                else:
                    pass
            
            else:
                pass

time_end = time.time()

print(superstring)
print('runtime: ', time_end-time_start)

# double check

QUERY_NUM = len(READS_CHECK)

present_in = 0

for read in READS_CHECK:
    
    if read in superstring:
        present_in += 1
    else:
        pass

print()

if present_in == QUERY_NUM:
    print('all reads present in superstring')

else:
    print('some reads were not incorporated:')
    print(READS)