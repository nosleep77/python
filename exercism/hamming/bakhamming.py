

#def distance(strand_a, strand_b):
  
  # if len(strand_a) != len(strand_b):
  #   raise ValueError("size not equal")

  #c = sum([ 1 for a in range(len(strand_a)) if strand_a[a] != strand_b[a] ])
  #c = list(filter(lambda x: x in strand_a, strand_b))

  #c = sum([ 1 for a,b in zip(strand_a,strand_b) if a != b ])
  #return c

## alternate solution
  # distance = 0

  # for index, letter in enumerate(strand_a):
  #       if letter != strand_b[index]:
  #           distance += 1

  # return distance


## good alternate solution
# def distance(strand_a, strand_b):
#     if len(strand_a) == len(strand_b):
#        return len(strand_a) - [i==j for i, j in zip(strand_a, strand_b)].count(True)
#     else:
#         raise ValueError("ValueError")

print(distance("GGACGGATTCTG", "AGGACGGATTCT"))

