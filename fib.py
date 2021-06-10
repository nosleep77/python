
def get_fib(n):

  a = [1,1]

  for i in range(n):
    a.append(a[-1] + a[-2])

  print(a)
  return a[n-1]

print(get_fib(3))