def factors(value):
  n = value
  i = 2
  factors = []
  while i * i <= value:
      if value % i:
          i += 1
      else:
          value //= i
          factors.append(i)
  if value > 1:
      factors.append(value)
  return factors

print(factors(2))

