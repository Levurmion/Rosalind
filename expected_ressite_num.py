# EXPECTED NUMBER OF RESTRICTION SITES

'''
Given a number n, a substring s, and A, array of numbers between 0 and 1:

Return and array B of length = len(A) where B[i] = the expected occurence of substring s within a superstring of length n with GC-content A[i]
'''
import math

n = 10
s = 'AG'
A = [0.25, 0.5, 0.75]

B = []

# for gc in A:

#     base_prob = {'G':gc/2,'C':gc/2,'A':(1-gc)/2,'T':(1-gc)/2}
#     P_s = 1

#     #calculate P_s
#     for base in s:
#         P_s = P_s*base_prob[base]
    
#     print(P_s)

exp_range = n//len(s)

P_AG = 1/16
P_notAG = 1-P_AG

exp_AG = 0

for exp in range(0,exp_range+1):
    
    num_bases_rem = 10-(exp*2)
    num_pos_2mers_rem = num_bases_rem-2+1

    P_exp = (P_AG)**exp * (P_notAG)**num_pos_2mers_rem
    exp_AG += P_exp

print(exp_AG)
    
    
    

