'''
def get_fib(n):

  a = [1,1]

  for i in range(n):
    a.append(a[-1] + a[-2])

  print(a)
  return a[n-1]
'''

def get_fib(n):

  a = 0
  b = 1

  for i in range(n):
    a, b = b, a+b
    
  yield a


n = 20

for i in range(n):
  print(f"{i}: {list(get_fib(i))}")

