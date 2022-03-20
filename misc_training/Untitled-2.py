def array_diff(a, b):

  for i in b:
    if i in a:
      a[:] = [item for item in a if item != i]
      #b[:] = [item for item in b if item != i]
  
  return a

print(array_diff([1,2,3],[1,2]))

## better version
def array_diff(a, b):
    return [x for x in a if x not in b]