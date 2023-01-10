# WOBBLE BASE PAIRING AND RNA SECONDARY STRUCTURE

'''
In previous exercises, we have only considered classical Watson-Crick basepairs. However, in real cases, U can bond with G in what is known as a wobble pair. We are now going to take this into account. In addition, we are going to restrict each base to be only able to pair with other bases that are at least 4 nucleotides away to take into account the limitations of RNA secondary structure.
'''

def count_structures(rna_string, memo={}):

    basepairs = {'A':'U', 'U':'A', 'G':'C', 'C':'G', 'U':'G', 'G':'U'}

    # base case for the substring being a constricted 4-nt section where all of the bases are too close to bond with each other
    if len(rna_string) <= 4:
        return 1

    # otherwise, continue recursion
    else:

        # count cases where base does not bond with anything
        no_bonding_count = count_structures(rna_string[1:])

        # count cases where base bonds with other bases at least 4-nt away
        total_bonding_count = 0

        for i in range(0,len(rna_string)-4):

            base = rna_string[i]
            before_base_substr = rna_string[:i]

            try:
                before_base_count = memo[before_base_substr]
            except KeyError:
                before_base_count = count_structures(before_base_substr)
                memo[before_base_substr] = before_base_count

            for j in range(i+4,len(rna_string)):

                if rna_string[j] == basepairs[base]:
                    left_rna_substr = rna_string[i+1:j]
                    right_rna_substr = rna_string[j+1:]
                    
                    # enquire for number of bondings possible with the left substring
                    try:
                        left_bonding_count = memo[left_rna_substr]
                    except KeyError:
                        left_bonding_count = count_structures(left_rna_substr)
                        memo[left_rna_substr] = left_bonding_count
                    
                    # enquire for number of bondings possible with the right substring
                    try:
                        right_bonding_count = memo[right_rna_substr]
                    except KeyError:
                        right_bonding_count = count_structures(right_rna_substr)
                        memo[right_rna_substr] = right_bonding_count

                    count_product = left_bonding_count * right_bonding_count * before_base_count
                    total_bonding_count += count_product
            
                else:
                    pass
        
        total_structures = no_bonding_count + total_bonding_count

        return total_structures


RNA_STRING = 'AUGCUAGUACGGAGCGAGUCUAGCGAGCGAUGUCGUGAGUACUAUAUAUGCGCAUAAGCCACGU'

print(count_structures('CGAUGCUAG'))

# 284850219977421

# 246403184217