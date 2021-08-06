from itertools import chain

class School:

  def __init__(self):
    self.s = {}

  def add_student(self, name, grade):
    self.s[name] = grade

  def roster(self):
    d = [self.slist(a) for a in set(self.s.values())]
    return list(chain.from_iterable(d))

  def grade(self, grade_number):
    return self.slist(grade_number)

  def slist(self, grade):
    return sorted([k for k,v in self.s.items() if v == grade])



# from itertools import chain
# from sortedcontainers import SortedDict, SortedList
# class School:
#     def __init__(self):
#         self.students = SortedDict()
#     def add_student(self, name, grade):
#         self.students.setdefault(grade, SortedList()).add(name)
#     def roster(self):
#         return list(chain.from_iterable(self.students.values()))
#     def grade(self, grade_number):
#         return self.students.get(grade_number, [])