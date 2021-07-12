class Robot:

  model = "T1000"

  def __init__(self, name="Tom", color="green", weight=30) -> None:
    self.name = name
    self.color = color
    self.weight = weight

  def intro(self):
    print(f"my name is {self.name}. color is {self.color}. weight is {self.weight}")

  @classmethod
  def get_model(cls):
    return cls.model

  @staticmethod
  def ranrobot():
    return "a random robot"

r1 = Robot("Jack","blue",45)
r1.intro()

Robot.model = "T2000"

print(f"model is {Robot.get_model()}")

print(f"model is {r1.ranrobot()}")