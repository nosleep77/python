from itertools import chain

def say(number):
  
  if number < 0 or number > 999999999999:
    raise ValueError("!")

  if number == 0:
    return "zero"

  nums = {
    1000000000: "billion",
    1000000:    "million",
    1000:       "thousand",
    100:        "hundred",
    90: "ninety-",    80: "eighty-",    70: "seventy-",    60: "sixty-",    50: "fifty-",    40: "forty-",
    30: "thirty-",    20: "twenty-",    19: "nineteen", 18: "eighteen", 17: "seventeen",
    16: "sixteen",  15: "fifteen",  14: "fourteen",  13: "thirteen",  12: "twelve",
    11: "eleven",  10: "ten", 9: "nine", 8: "eight", 7: "seven", 6: "six",
    5: "five",  4: "four", 3: "three", 2: "two", 1: "one",
  }

  tys = [val for key,val in nums.items() if key < 100 and key > 19]

  c = [" ", " "]
  while number > 0:
    for i in nums.keys():
      # if number == 0:
      #   break
      x = 0
      if number >= i:
        while number >= i:
          number -= i
          x += 1
        if i >= 100:
          c.append(say(x))
          c.append(" ")
        # if (c[-2] in tys) and (i > 0 and i < 10):
        #     c.append("-")
        c.append(nums[i])
        c.append(" ")
        
  c = "".join(list(chain.from_iterable(c))).strip().rstrip("-")

  return c.replace("- ","-")

print(say(50599))
