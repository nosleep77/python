"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type



# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = None
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None
"""

'''
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

def score(dice, category):
   
  if category == "ONES":
    return dice.count(1) * 1

  if category == "TWOS":
    return dice.count(2) * 2

  if category == "THREES":
    return dice.count(3) * 3

  if category == "FOURS":
    return dice.count(4) * 4

  if category == "FIVES":
    return dice.count(5) * 5

  if category == "SIXES":
    return dice.count(6) * 6


  if category == "FULL_HOUSE":
    threenum, twonum = 0,0
    for a in dice:
      if dice.count(a) == 3:
        threenum = a
      if dice.count(a) == 2:
        twonum = a

    if sum(dice) == (threenum*3) + (twonum*2):
      return sum(dice)
    else:
      return 0


  if category == "FOUR_OF_A_KIND":
    for a in dice:
      if dice.count(a) >= 4:
        return 4*a
    return 0


  if category == "LITTLE_STRAIGHT":
    if sorted(dice) == [1,2,3,4,5]:
      return 30
    return 0


  if category == "BIG_STRAIGHT":
    if sorted(dice) == [2,3,4,5,6]:
      return 30
    return 0


  if category == "CHOICE":
    return sum(dice)


  if category == "YACHT":
    for a in dice:
      if dice.count(a) == 5:
        return 50
    return 0

'''

ONES = lambda x: x.count(1)*1

def score(dice, category):
  return category(dice)