class Matrix:
    def __init__(self, matrix_string):
      self.matrix_string = [[int(i) for i in x.split()] for x in matrix_string.splitlines()]

    def row(self, index):
      return self.matrix_string[index-1]

    def column(self, index):
      return [a[index-1] for a in self.matrix_string]
