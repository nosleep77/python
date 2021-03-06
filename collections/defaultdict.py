
from collections import defaultdict

'''
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)


from collections import defaultdict
tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
print(some_dict)
'''

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3

# check key that exists
print(d['c'])

# check key that does not exist - no error
print(d['d'])

