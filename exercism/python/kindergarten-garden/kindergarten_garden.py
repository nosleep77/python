S = ("Alice", "Bob", "Charlie", "David", 
  "Eve", "Fred", "Ginny", "Harriet", 
  "Ileana", "Joseph", "Kincaid", "Larry")
POTS = ["Grass", "Clover", "Radishes", "Violets"]

class Garden:

  def __init__(self, diagram, students=S):
    self.students = sorted(students)
    self.diagram = diagram.split("\n")

  def plants(self, student):
    x = self.students.index(student)*2
    rows = [self.diagram[0][a] for a in range(x,x+2)] + [self.diagram[1][a] for a in range(x,x+2)]
    return [b for a in rows for b in POTS if b.startswith(a)]

