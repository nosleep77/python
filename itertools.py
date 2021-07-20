# itertools
# product, permutations, combinations, accumulate, groupby, infinite iterators

## also see library: more_itertools

# cartesian product
'''
from itertools import product

a = [1,2]
b = [3,4]

prod = product(a,b)
#prod = product(a,b, repeat=2)
print(list(prod))

## output
# [(1, 3), (1, 4), (2, 3), (2, 4)]
'''


# permutations
'''
from itertools import permutations
a = [1,2,3]
perm = permutations(a)
#perm = permutations(a, 3)
print(list(perm))

## output
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
'''


# combinations
'''
from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

## output
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
'''


# accumulate
'''
from itertools import accumulate
import operator
a = [1,2,5,3,4]
# specifying mul it will multiply otherwise default is to add
# acc = accumulate(a, func=operator.mul)
# this return the max
# acc = accumulate(a, func=max)

acc = accumulate(a)

# print(a)
print(list(acc))

## output
# [1, 3, 8, 11, 15]
'''


# groupby
'''
from itertools import groupby
def smaller_than_3(x):
  return x < 3
a = [1,2,3,4]
#group1 = groupby(a, key=smaller_than_3)
group1 = groupby(a, key= lambda x: x<3)
for key, value in group1:
  print(key, list(value))

## output
# True [1, 2]
# False [3, 4]
'''




# from itertools import count,cycle,repeat
'''
 infinite loop starts at 1
for i in count(1):
  print(i)
'''

'''
a = [1,2,3,4]
for i in cycle(a):
  print(i)
'''

'''
for i in repeat(1, 4):
  print(i)
'''



