def check_inequality(sides):
  x = sides[0]
  y = sides[1]
  z = sides[2]

  if not (x+y>z) or not (x+z>y) or not (y+z>x):
    return False,x,y,z
  else:
    return True,x,y,z


def equilateral(sides):
  res,x,y,z = check_inequality(sides)

  if not res:
    return False

  if x == y == z:
    return True
  else:
    return False


def isosceles(sides):
  res,x,y,z = check_inequality(sides)

  if not res:
    return False

  if len(set([str(x) for x in sides])) == len([str(x) for x in sides]):
    return False
  else:
    return True


def scalene(sides):
  res,x,y,z = check_inequality(sides)

  if not res:
    return False
  
  if x != y and x != z and y != z:
    return True
  else:
    return False





## alternate solution
# def equilateral(sides):
#     """Returns True if it is an equilateral triangle, otherwise return False."""
#     return len(set(sides)) == 1 and 0 not in set(sides)
# def isosceles(sides):
#     """Returns True if it is an isosceles triangle, otherwise return False."""
#     sides.sort()
#     return (len(set(sides)) <= 2) and (sum(sides[:2]) >= sides[2])
# def scalene(sides):
#     """Returns True if it is a scalene triangle, otherwise return False."""
#     sides.sort()
#     return (len(set(sides)) == 3) and (sum(sides[:2]) >= sides[2])


## alternate solution
# def equilateral(sides: list) -> bool:
#     return len(set(sides)) == 1 and any(sides)
# def isosceles(sides: list) -> bool:
#     return 3 > len(set(sides)) >= 1 and sum(sides)-max(sides) >= max(sides)
# def scalene(sides: list) -> bool:
#     return len(set(sides)) == 3 and sum(sides)-max(sides) >= max(sides)


## alternate solution
# def equilateral(sides):
#     return 0 < sides[0] == sides[1] == sides[2]
# def isosceles(sides):
#     s = sorted(sides)
#     return s[1] == s[2] or (s[0] == s[1] and s[2] <= 2*s[1])
# def scalene(sides):
#     s = sorted(sides)
#     return s[0] != s[1] != s[2] and s[2] <= s[0]+s[1]