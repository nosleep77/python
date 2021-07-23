def factors(min_factor, max_factor, num):    
  return [[f1, num//f1] for f1 in range(min_factor, int(num**0.5)+1) 
  if num%f1==0 and num//f1 in range(min_factor, max_factor+1)]


def largest(min_factor, max_factor):
  if min_factor > max_factor:
    raise ValueError("!!")
  pal = sorted(set([ x*y for x in range(min_factor,max_factor+1) for y in range(min_factor,max_factor+1) if str(x*y) == str(x*y)[::-1]]))
  try:
    f = factors(min_factor,max_factor,max(pal))
  except ValueError:
    return None, []
  return max(pal), f
  

def smallest(min_factor, max_factor):
  if min_factor > max_factor:
    raise ValueError("!!")
  pal = sorted(set([ x*y for x in range(min_factor,max_factor+1) for y in range(min_factor,max_factor+1) if str(x*y) == str(x*y)[::-1]]))
  try:
    f = factors(min_factor,max_factor,min(pal))
  except ValueError:
    return None, []
  return min(pal), f
