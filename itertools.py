# itertools
# product, permutations, combinations, accumulate, groupby, infinite iterators

# cartesian product

'''
from itertools import product

a = [1,2]
b = [3,4]

prod = product(a,b, repeat=2)
print(list(prod))
'''

'''
from itertools import permutations
a = [1,2,3]
perm = permutations(a, 3)
print(list(perm))
'''

'''
from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))
'''

'''
from itertools import accumulate
import operator
a = [1,2,5,3,4]
# specifying mul it will multiply otherwise default is to add
acc = accumulate(a, func=operator.mul)
# this return the max
acc = accumulate(a, func=max)

print(a)
print(list(acc))
'''

'''
from itertools import groupby
def smaller_than_3(x):
  return x < 3
a = [1,2,3,4]
#group1 = groupby(a, key=smaller_than_3)
group1 = groupby(a, key= lambda x: x<3)
for key, value in group1:
  print(key, list(value))
'''

'''
from itertools import count,cycle,repeat

# infinite loop starts at 1
for i in count(1):
  print(i)

a = [1,2,3,4]
for i in cycle(a):
  print(i)

for i in repeat(1, 4):
  print(i)
'''