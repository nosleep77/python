def distance(strand_a, strand_b):
  
  if len(strand_a) != len(strand_b):
    raise ValueError("size not equal")

  #return sum([ 1 for a,b in zip(strand_a,strand_b) if a != b ])

  return [ 1 for a,b in zip(strand_a,strand_b) if a != b ].count(True)

print(distance("GGACGGATTCTG", "AGGACGGATTCT"))