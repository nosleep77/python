matrix_string = "89 1903 3\n18 3 1\n9 4 800"

### list comprehension
#result = [[int(i) for i in x.split()] for x in matrix_string.splitlines()]
result = [int(i) for i in matrix_string.splitlines() for x in x.split()]
### unroll once
# result = []
# for x in matrix_string.splitlines():
#     result.append([int(i) for i in x.split()])
### unroll twice
# result = []
# for x in matrix_string.splitlines():
#     row = []
#     for i in x.split():
#         row.append(int(i))
#     result.append(row)

print(result)