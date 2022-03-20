'''
colours =  {"Red" : 198, "Green" : 170, "Blue" : 160}
for key, value in colours.items():
    print(key, value)
'''

## regular dictionary also remembers order

from collections import OrderedDict

colours = OrderedDict([("Green", 170), ("Blue", 160), ("Red", 198)])
for key, value in colours.items():
    print(key, value)