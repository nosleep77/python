def saddle_points(matrix):

  if matrix == []:
    return []

  if not all(len(ele) == len(matrix[0]) for ele in matrix):
    raise ValueError("elements of matrix irregular")

  rowsize = len(matrix)
  colsize = len(matrix[0])

  cols = [[matrix[b][a] for b in range(rowsize)] for a in range(colsize)]
  return [ {"row": a+1, "column": b+1} for a in range(rowsize) 
          for b in range(colsize) if max(matrix[a]) == min(cols[b]) ]

# ## converts rows to columns in list
# b = [[89, 1903, 3], [18, 3, 1], [9, 4, 800]]
# list(zip(*b))
# # output
# [(89, 18, 9), (1903, 3, 4), (3, 1, 800)]


## alternate solution
# from more_itertools import all_equal
# def saddle_points(mat):
#     if not all_equal(map(len, mat)):
#         raise ValueError('!!')

#     s1 = [max(row) for row in mat] 
#     s2 = [min(col) for col in zip(*mat)]

#     return [
#         {"row": i, "column": j}
#         for i, (row, srow) in enumerate(zip(mat, s1), 1)
#         for j, (col, scol) in enumerate(zip(row, s2), 1)
#         if col == srow == scol
#     ]