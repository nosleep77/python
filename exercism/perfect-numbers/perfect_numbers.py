def classify(number):

  if number <= 0:
    raise ValueError("has to be positive integer")

  al_sum = sum([i for i in range(1,number+1) if number%i==0][:-1])

  if al_sum == number:
    return "perfect"
  elif al_sum > number:
    return "abundant"
  else:
    return "deficient"