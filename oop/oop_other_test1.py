
class Math:

  def __init__(self, num):
    self.num = num

  ## override the default eq operator
  def __eq__(self, other):
    return self.num == other.num
    
    

# m1.name = "dodo"
# print(m1.add5(5))
# print(m1.name)

#print(Math(5).test() + Math(5).test())

#print(m1.__eq__(5))

#Math(5) + Math(3)

print(Math(7) == Math(6))