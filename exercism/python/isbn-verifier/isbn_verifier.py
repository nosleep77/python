import re

def is_valid(isbn):
  
  pattern = r"^\d(-|)\d{3}(-|)\d{5}(-|)(X|\d)$"
  if not re.search(pattern, isbn):
     return False
  
  isbn1 = list(isbn.replace("-",""))

  if isbn1[-1] == "X":
    isbn1[-1] = "10" 
  
  d = sum([ (int(isbn1[a])*(10-a)) for a in range(len(isbn1)) ])

  return d % 11 == 0


print(is_valid("3-598-21507-X"))


## alternate solution
# def is_valid(isbn):
#     s = isbn.replace("-","")
#     if len(s) == 10 and s[:-1].isdigit() and (s[-1] == "X" or s[-1].isdigit()):
#         s = ((" ".join(s)).replace("X", "10")).split()
#         return (sum([int(s[i])*(10-i) for i in range(len(s))]) % 11) == 0
#     else:
#         return False



## alternate solution
# def is_valid(isbn):
#     stripped_isbn = isbn.replace("-", "")
#     if len(stripped_isbn) != 10 or "X" in stripped_isbn[:-1]:
#         return False
#     try:                    
#       digits = [ int(n) if n != "X" else 10 for n in stripped_isbn]
#     except ValueError:      
#       return False    
#     return sum( [ d * (10-i) for i, d in enumerate(digits)] ) % 11 == 0



## alternate solution
# import re
# def is_valid(isbn):
#     p = re.compile(r'''
#         ^(\d)
#         [\s\-]?
#         (\d{3})
#         [\s\-]?
#         (\d{5})
#         [\s\-]?
#         ([xX\d])
#         \s*$
#     ''',re.VERBOSE)
#     match = p.match(isbn)
#     if match is None:
#         return False
#     else:
#         sanitised_isbn = "".join(match.groups()).lower()
#         return sum([pos * (10 if int_char == 'x' else int(int_char)) for pos, int_char in zip(range(10,0,-1),sanitised_isbn)]) % 11 == 0


