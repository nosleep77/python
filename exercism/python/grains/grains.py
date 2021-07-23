def square(number):
  if number < 1 or number > 64:
  #if number not in range(1,65):
    raise ValueError("number out of range")
  return 2**(number-1)


def total():
  squares = 64
  return (1*(1-2**squares)) // (1-2)
