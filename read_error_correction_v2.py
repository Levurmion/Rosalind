# Error Correction in Reads

'''
Sequencing technologies are not 100% foolproof. Every now and then, either the machine or sample preparation protocols make errors in generating a faithful readable representation of the sequenced fragment. Most of the time, these errors are minor - manifesting as single point mutations that can be identified by comparing multiple similar reads (which can also be in the form of its complement) to obtain a majority consensus sequence for the species. This is why sequencing depth - the number of times each substring of a genome is sequenced into reads on average, is important as it provides redundant information for the read correction algorithms to work on as to generate a faithful copy of the original sample.

In this example, given a collection of DNA reads of equal length, return a list of all corrections in the form 'old read' -> 'new read". For each read in the dataset, one of the following applies:

- the read was correctly sequenced and appears in the dataset AT LEAST TWICE (possibly as its reverse complement)
- the read has a single point mutation, appears in the dataset only exactly once, thus exhibiting a Hamming distance = 1 with respect to exactly one correct read in the dataset (or its reverse complement)
'''

from Bio import SeqIO

# function to generate reverse complement of reads
def rev_complement(string):

    revc = ''

    for base in string[::-1]:

        if base == 'A':
            revc += 'T'
        elif base == 'T':
            revc += 'A'
        elif base == 'G':
            revc += 'C'
        elif base == 'C':
            revc += 'G'
    
    return revc


# Hamming distance
def hamm_dist(string1,string2):

    string_len = len(string1)

    hamm_distance = 0

    for i in range(0,string_len):
        
        if string1[i] == string2[i]:
            pass
        elif string1[i] != string2[i]:
            hamm_distance += 1
    
    return hamm_distance



file = list(SeqIO.parse('rosalind_corr.txt','fasta'))

READS = []

for record in file:
    READS.append(str(record.seq))

# print('read library: ', READS)

correct_READS = []
incorrect_READS = []

lib_size = len(READS)


# find reads that only show up once
for i in range(0,len(READS)):

    read = READS[i]

    only_once = True

    read_revc = rev_complement(read)

    remREADS = list.copy(READS)
    remREADS.remove(read)

    for other_read in remREADS:

        if read == other_read:
            only_once = False
            break
        elif read_revc == other_read:
            only_once = False
            break
        else:
            pass
    
    if only_once == True:
        incorrect_READS.append(read)
    elif only_once == False:
        correct_READS.append(read)
    else:
        pass
   
# correct reads left in original list
# perform corrections

correct_reads_len = len(correct_READS)
incorrect_READS = list(set(incorrect_READS))
correct_READS = list(set(correct_READS))

corrections = []

corrected_reads = 0

for wrong_read in incorrect_READS:

    wrong_read_revc = rev_complement(wrong_read)
    corrected = False

    for read in correct_READS:

        if hamm_dist(wrong_read,read) == 1:
            corrections.append([wrong_read,read])
            corrected = True
        
        elif hamm_dist(wrong_read_revc,read) == 1:
            read_revc = rev_complement(read)
            corrections.append([wrong_read,read_revc])
            corrected = True

        else:
            pass
    
    if corrected == True:
        corrected_reads += 1

# print results
with open('error_corr.txt','w') as file:
    
    for pair in corrections:
        line = pair[0] + '->' + pair[1]
        file.write(line + '\n')

print('library size: \t', lib_size)
print('correct reads: \t', correct_reads_len)
print('unique correct reads: \t', len(correct_READS))
print('incorrect reads: \t', len(incorrect_READS))
print('corrections:\t', len(corrections))
print('actual corrected wrong reads: \t', corrected_reads)



    
