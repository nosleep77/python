def saddle_points(matrix):

  cols = [[matrix[b][a] for b in range(3)] for a in range(3)]
  spoints = []

  for a in range(3):
    row = matrix[a]
    for b in range(3):
      col = cols[b]
      if max(row) == min(col):
        #spoints.append({"row": row.index(max(row))+1, "column": col.index(min(col))+1})
        spoints.append({"row": a+1, "column": b+1})

  return spoints


# matrix = [[9, 8, 7], 
#           [5, 3, 2], 
#           [6, 6, 7]]
matrix = [[4, 5, 4], 
          [3, 5, 5], 
          [1, 5, 4]]
print(saddle_points(matrix))


    # [
    #     {"row": 1, "column": 2},
    #     {"row": 2, "column": 2},
    #     {"row": 3, "column": 2},
    # ]

    # def test_can_identify_single_saddle_point(self):
    #     matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
    #     self.assertEqual(
    #         sorted_points(saddle_points(matrix)),
    #         sorted_points([{"row": 2, "column": 1}]),
    #     )

