import random
from random import choice, seed
from string import ascii_uppercase, digits

class Robot:

  list_names = set()

  def __init__(self):
    self.name = self.gen_name()

  def gen_name(self):
    alpha2  = ''.join(choice(ascii_uppercase) for i in range(2))
    digits3 = ''.join(choice(digits) for i in range(3))
    return alpha2+digits3


  def reset(self):
    self.name = self.gen_name()
    self.list_names.add(self.name)

    if self.name in self.list_names:
        self.name = self.gen_name()
  
  


# Set a seed
seed = "Totally random."

# Initialize RNG using the seed
random.seed(seed)

# Call the generator
robot = Robot()
name = robot.name

# Reinitialize RNG using seed
random.seed(seed)

# Call the generator again
robot.reset()
name2 = robot.name
print(f"name {name} name2 {name2}")


