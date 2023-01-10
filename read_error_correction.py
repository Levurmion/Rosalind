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

print('read library: ', READS)

correct_READS = []

idx = 0
for read in READS:

    read_revc = rev_complement(read)

    remREADS = list.copy(READS)
    del remREADS[idx]

    correct_species = False

    for other_read in remREADS:

        if read == other_read:
            # READS.remove(other_read)
            correct_species = True
            # correct_species.append(other_read)

        elif read_revc == other_read:
            # READS.remove(other_read)
            correct_species = True
            # correct_species.append(other_read)

        else:
            pass
    
    if correct_species == True and read not in correct_READS:
        # READS.remove(read)
        correct_READS.append(read)
    
    else:
        pass

    idx += 1


print('correct reads: ',correct_READS)
print('remaining reads: ',READS)

correction_list = []
cannot_correct = []

for wrong_read in READS:

    corrections = []

    for correct_species in correct_READS:

        correct_read = correct_species
        correct_read_revc = rev_complement(correct_read)

        wrong_read_hamm = hamm_dist(wrong_read,correct_read)
        wrong_read_revc_hamm = hamm_dist(wrong_read,correct_read_revc)

        if wrong_read_hamm == 1:
            corrections = [wrong_read,correct_read]
        elif wrong_read_revc_hamm == 1:
            corrections = [wrong_read,correct_read_revc]
        else:
            pass
    
    if corrections != []:
        correction_list.append(corrections)
    else:
        cannot_correct.append(wrong_read)

print('corrections: ', correction_list, '\n')

print('output: ')
for correction in correction_list:
    print(correction[0],'->',correction[1])

print('cannot correct: ',cannot_correct)

# for read in cannot_correct:
    
#     other_reads = list.copy(cannot_correct)
#     other_reads.remove(read)

#     for other in other_reads:

#         print('hamming distance', read, '->', other, ': ', hamm_dist(read,other))