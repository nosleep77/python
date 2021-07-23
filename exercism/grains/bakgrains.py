def square(number):
  if number <= 0 or number > 64:
    raise ValueError("cannot be <= 0")
  return 2**(number-1)


def total():
  squares = 64
  return (1*(1-2**squares)) // (1-2)


#(square(3), 4)
#print(square(16))

print(total())

#1*2**(number-1)
#square(16), 32768)