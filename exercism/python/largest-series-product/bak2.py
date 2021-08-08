# import numpy as np

# def largest_product(series, size):
#   if size <= len(series) and size > 0:
#     a = [series[a:a+size] for a in range(len(series)-size+1)]
#     return max([np.prod([ int(char) for char in b ]) for b in a])
#   elif size==0:
#     return 1
#   else:
#     raise ValueError("something is up")


import math
def largest_product(series, size):
    if size < 0: raise ValueError('Size must be a non-negative integer.')
    return max([math.prod([int(j) for j in list(series[i:i+size])]) for i in range(len(series)-size+1)])


print(largest_product(largest_product("123", 0)))

    # def test_reports_1_for_empty_string_and_empty_product_0_span(self):
    #     self.assertEqual(largest_product("", 0), 1)

    # def test_reports_1_for_nonempty_string_and_empty_product_0_span(self):
    #     self.assertEqual(largest_product("123", 0), 1)