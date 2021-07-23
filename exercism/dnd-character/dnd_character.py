import random
import math
from functools import reduce

class Character:

  def get_score(self):
    list1 = sorted(list( random.randint(1,6) for x in range(4) ), reverse=True)
    list1.pop()
    return reduce(lambda x,y: x+y,list1)

  def __init__(self):
    self.strength = self.get_score()
    self.dexterity = self.get_score()
    self.constitution = self.get_score()
    self.intelligence = self.get_score()
    self.wisdom  = self.get_score()
    self.charisma = self.get_score()
    self.hitpoints = modifier(self.constitution) + 10

  def ability(self):
    return self.get_score()


def modifier(const):
  return math.floor((const - 10) / 2)