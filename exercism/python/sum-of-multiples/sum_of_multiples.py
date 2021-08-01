def sum_of_multiples(limit, multiples=[0,0]):
  
  # b = set()
  # for a in multiples:
  #   for c in range(a,limit):
  #     if a != 0 and c%a==0:
  #       b.add(c)

  return sum(
         set(
           c for a in multiples for c in range(a,limit) if (a != 0) and (c%a==0)
           )
           )

  #return sum(b)
