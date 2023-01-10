# k-Mer Composition

'''
k-Mers are k-long substrings of DNA strings. A genetic string of length n can be seen as composed of n-k+1 overlapping k-mers. The k-mer composition of a genetic string encodes the number of times each unique k-mer occurs in the string. As it may be intuitively obvious, longer k-mers provide more robust "fingerprints" for the string's identity as these would better represent entire "words" that compose the string instead of individual symbols. As such, k-mer based read assembly algorithms form the core of many short-read sequencing workflows.

In this example, given a DNA string, provide the 4-mer composition of the string in an array A in lexicographic order.
'''

from Bio import SeqIO

def generate_kmers(k,kmer=''):

    global KMER_LIST

    bases = ['A','C','G','T']

    if len(kmer) == k:
        KMER_LIST.append(kmer)
        return
    
    else:
        for base in bases:
            generate_kmers(k,kmer + base)



global KMER_LIST
KMER_LIST = []
k = 4

generate_kmers(k)

KMER_DICT = {}

idx = 0

for kmer in KMER_LIST:
    KMER_DICT[kmer] = idx
    idx += 1


file = list(SeqIO.parse('rosalind_kmer.txt','fasta'))
    
DNA_STRING = file[0].seq

A = [0]*len(KMER_LIST)

for idx in range(0,len(DNA_STRING)-k+1):
    
    substring = DNA_STRING[idx:idx+k]
    
    A[KMER_DICT[substring]] += 1


for num in A:
    print(num,end=' ')