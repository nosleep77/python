class Robot:

  def __init__(self, name="Tom", color="green", weight=30) -> None:
    self.name = name
    self.color = color
    self.weight = weight

  def intro(self):
    print(f"my name is {self.name}. color is {self.color}. weight is {self.weight}")


r1 = Robot("Jack","blue",45)
r1.intro()