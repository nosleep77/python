import numpy as np

def largest_product(series, size):

  if series == "" and size != 0 or size > len(series) or size < 0:
    raise ValueError("something is up")

  if size <= len(series) and size > 0 and len(series) > 0:

    a = [series[a:a+size] for a in range(len(series)-size+1)]
    return max([np.prod([ int(char) for char in b ]) for b in a])

    #return max(d)

  else:
    #raise ValueError("something is up")
    return 1


print(largest_product("0123456789", 2))