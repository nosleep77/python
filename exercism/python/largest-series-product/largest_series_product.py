import math

def largest_product(series, size):
  if size <= len(series) and size > 0:
    a = [series[a:a+size] for a in range(len(series)-size+1)]
    return max([math.prod([ int(char) for char in b ]) for b in a])
  elif size==0:
    return 1
  else:
    raise ValueError("something is up")
