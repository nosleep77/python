def is_armstrong_number(number):

  numlen = len(number)

  return sum(int(a)**numlen for a in str(number)) == number

