from functools import reduce

def factors(n): 

  return reduce(list.__add__, 
                #([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))


print(sorted(factors(9009)))

#[1, 3, 7, 9, 11, 13, 21, 33, 39, 63, 77, 91, 99, 117, 143, 231, 273, 429, 693, 819, 1001, 1287, 3003, 9009]

num=9009
mn=10
mx=99
[[f1, num//f1] for f1 in range(mn, int(num**0.5)+1) if num%f1==0 and num//f1 in range(mn, mx+1)]

num=9009
mn=10
mx=99
[[77, 9009//77] for 77 in range(10, int(9009**0.5)+1) if 9009%77==0 and 9009//77 in range(10, 100)]

## the factors have to be in range from min_factor to max_factor