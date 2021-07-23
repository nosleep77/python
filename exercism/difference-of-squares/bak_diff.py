from functools import reduce

def square_of_sum(number):

  #return sum([a for a in range(number+1)])**2

  # b = 0
  # for a in range(number+1):
  #   b += a

  # return b**2

  # return reduce(lambda x,y: x+y, [a for a in range(number+1)])**2

  return sum([a for a in range(number+1)])**2


def sum_of_squares(number):
  # return sum([a**2 for a in range(number+1)])
    pass


def difference_of_squares(number):
    pass


print(square_of_sum(5))