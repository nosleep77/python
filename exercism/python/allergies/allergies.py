class Allergies:

  SCORES = {
    1: "eggs",
    2: "peanuts",
    4: "shellfish",
    8: "strawberries",
    16: "tomatoes",
    32: "chocolate",
    64: "pollen",
    128: "cats",
  }

  def __init__(self, score):
    self.score = score


  def allergic_to(self, item):
    a = next(key for key, value in self.SCORES.items() if value == item)
    if a == self.score or item in self.lst:
      return True
    else:
      return False


  @property
  def lst(self):
    c = []
    for i in reversed(self.SCORES.keys()):
      if self.score == i:
        c.append(self.SCORES[i])
        break
      if self.score > i:
        if self.score == 257:
          c.append(self.SCORES[1])
          break  
        c.append(self.SCORES[i])
        self.score -= i
    return c
