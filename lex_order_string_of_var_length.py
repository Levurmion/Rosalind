# ORDERING STRINGS OF VARYING LENGTHS LEXICOGRAPHICALLY

'''
Given an ordered set of alphabets containing at most 12 symbols, give all of its possible permutations of length n in lexicographic order.
'''

def lex_perm_length_n(symbols,n,perm='',result=[]):

    if len(perm) == n:
        result.append(perm)
        
    else:
        for symbol in symbols:
            if (perm + ' '*(n-len(perm))) not in result and len(perm) > 0:
                result.append(perm + ' '*(n-len(perm)))
            lex_perm_length_n(symbols,n,perm + symbol,result)

        return result



input = 'F S N P M J B I V O Y X'
SYMBOLS = input.split(' ')
n = 3

permlist = lex_perm_length_n(SYMBOLS,n)

with open('lex_order_string_varlength.txt','w') as file:

    for perm in permlist:
        file.write(perm + '\n')