# CALCULATING EXPECTED OFFSPRING

'''
Given 6 non-negative integers [i1,i2,i3,i4,i5,i6] corresponding to the initial populations of [AA-AA,AA-Aa,AA-aa,Aa-Aa,Aa-aa,aa-aa] couples, find the expected number of offspring exhibiting the dominant phenotype (AA or Aa) with the assumption that each couple bears esactly two offspring.
'''

DATA = '17381 18656 18271 19043 17981 18528'
couples = [int(x) for x in DATA.split(' ')]

total_couples = sum(couples)
weighted_prob_dom_offspring = [0]*6

weighted_prob_dom_offspring[0] = (couples[0]/total_couples)*1
weighted_prob_dom_offspring[1] = (couples[1]/total_couples)*1
weighted_prob_dom_offspring[2] = (couples[2]/total_couples)*1
weighted_prob_dom_offspring[3] = (couples[3]/total_couples)*0.75
weighted_prob_dom_offspring[4] = (couples[4]/total_couples)*0.5
weighted_prob_dom_offspring[5] = 0

total_offspring = total_couples*2

expected_dom_offspring = total_offspring * sum(weighted_prob_dom_offspring)

print(weighted_prob_dom_offspring)
print(expected_dom_offspring)
