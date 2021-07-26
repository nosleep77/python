from collections import Counter


# examples of valid words
# one, 1, Go, GO, Stop, don't, can't
# regex pattern


# separator
# space, comma, :, 

# colours = (
#     ('Yasoob', 'Yellow'),
#     ('Ali', 'Blue'),
#     ('Arham', 'Green'),
#     ('Ali', 'Black'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )

colours = ("one fish two fish red fish blue fish")

favs = Counter(color in colours)
print(favs)
# Output: Counter({
#    'Yasoob': 2,
#    'Ali': 2,
#    'Arham': 1,
#    'Ahmed': 1
# })