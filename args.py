'''
def multiargs(*args):
  a = 0
  for i in args:
    a = a + i
  return a

print(multiargs(2,2,2))
'''

'''
## using reduce
from functools import reduce
n = [4,3,2,1]
print(reduce(lambda x,y: x+y, n))
'''

