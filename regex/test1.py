import re

# sentence = 'Start a sentence and then bring it to an end'
# pattern = re.compile(r'abc')
# matches = pattern.finditer()

# isbn = re.compile("(?:[0-9]{3}-)?[0-9]{1,5}-[0-9]{1,7}-[0-9]{1,6}-[0-9]")

# regex = "(?:ISBN(?:-1[03])?:? )?(?=[-0-9 ]{17}$|[-0-9X ]{13}$|[0-9X]{10}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]?(?:[0-9]+[- ]?){2}[0-9X]$"


# isbn = "3-598-21507-X"
# print(isbn)
# if (re.search(r'^[\dX-]{13}$', isbn)):
#   print("match 1")

# if (re.search(r'^\d{1,5}-\d{1,7}-\d{1,5}-[\dX]$', isbn) and len(isbn) == 13):
#   print("match 2")

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

#pattern = "^\d\d[A-Z][a-z]$"
#text = "23Fg"
# pattern = "^\D\D[A-Z][a-z]$"
# text = "\#Fg"
# pattern = "^\s\s[A-Z][a-z]$"
# text = "\n\tFg"

# + means unlimited number of said chars
#pattern = "[0-9]+"
#text = "2"

# exactly 3 of the type of chars
#pattern = "^[0-9]{3}$"
#text = "222"

## ISBN-10
#pattern = r"^\d(-|)\d{3}(-|)\d{5}(-|)(X|\d)$"
#text = "3-598-21507-X"
#text = "359821507X"

# pattern = '^a...s$'
# test_string = 'abyss'

# pattern = '^a.*s$'
# text = 'abds342#$4fsdss'

# pattern = "[0-39]"
# text = "9"


#pattern = r"\AWho.*\s\d+"
# pattern = r"\w+"
# text = "Who is there far 0123"

# #x = re.search(pattern, text)
# x = re.split(pattern, text)
# print(x)

txt = "The rain in Spain"
x = re.search(r"ra?", txt)
print(x)