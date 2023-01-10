# ALTERNATIVE SPLICING

from math import comb

n = 1971
m = 969

combination_sum = 0

for k in range(m,n+1):
    combination_sum += comb(n,k)

print(combination_sum%1000000)