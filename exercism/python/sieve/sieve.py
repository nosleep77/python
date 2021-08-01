def primes(limit):

  prime = [i for i in range(2,limit+1)]
  p = 2

  while p <= limit:

    for i in range(p*p,limit+1,p):
      try:
        a = prime.index(i)
      except ValueError:
        continue
      if prime[a] != 0:
        prime[a] = 0

    p += 1
  
  return [x for x in prime if x != 0]


# def primes(limit):
# 	potential_primes = [True] * (limit+1)
# 	# 0 and 1 are not primes
# 	potential_primes[0:2] = [False] * 2
# 	primes = []
# 	for counter, value in enumerate(potential_primes):
# 		if value:
# 			# If we reached this, the current value is prime
# 			primes.append(counter)
# 			# Mark all multiples of the current prime as composite
# 			potential_primes[counter*2:limit+1:counter] = [False] * len(range(counter*2, limit+1, counter))
# 	return primes

# def primes(limit):
#     potential_primes = set(range(2, limit+1))

#     for p in range(2, limit+1):
#         if p in potential_primes:           
#             potential_primes -= set(range(2*p, limit+1, p))
            
#     return list(potential_primes)