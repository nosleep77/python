class Garden:

  s = ["Alice", "Bob", "Charlie", "David", 
    "Eve", "Fred", "Ginny", "Harriet", 
    "Ileana", "Joseph", "Kincaid", "Larry"]
  pots = ["Grass", "Clover", "Radishes", "Violets"]

  def __init__(self, diagram, students=s):
    self.students = sorted(students)
    self.diagram = diagram.split("\n")

  def plants(self, student):
    x = self.students.index(student)*2
    rows = [self.diagram[0][a] for a in range(x,x+2)] + [self.diagram[1][a] for a in range(x,x+2)]
    return [b for a in rows for b in self.pots if b.startswith(a)]

