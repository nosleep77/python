
import math

def score(x, y):
	distance = math.sqrt(x**2 + y**2)
	points = {
		distance > 10: 0,
		distance <= 10: 1,
		distance <= 5: 5,
		distance <= 1: 10,
	}
	return points[True]

'''
def score(x, y):

  # x is in inner circle
  x_inner = (x <= 0.7 and x >= -0.7) 
  # x is in middle circle
  x_middle = (x > 0.7 or x < -0.7) and (x <= 3.5 or x >= -3.5)
  # x is in outer circle
  x_outer = (x > 3.5 or x < -3.5) and (x <= 7.0 or x >= -7.0)
  # x lands outside the target
  x_null = (x > 7.0 or x < -7.0)

  # y is in inner circle
  y_inner = (y <= 0.7 and y >= -0.7) 
  # y is in middle circle
  y_middle = (y > 0.7 or y < -0.7) and (y <= 3.5 or y >= -3.5)
  # y is in outer circle
  y_outer = (y > 3.5 or y < -3.5) and (y <= 7.0 or y >= -7.0)
  # y lands outside the target
  y_null = (y > 7.0 or y < -7.0)

  if x_null or y_null:
    return 0

  if x_inner:
    if y_inner:
      return 10
    if y_middle:
      return 5
    if y_outer:
      return 1
    if y_null:
      return 0

  if x_middle:
    if y_inner:
      return 5
    if y_middle:
      return 5
    if y_outer:
      return 1
    if y_null:
      return 0

  if x_outer:
    if y_inner:
      return 1
    if y_middle:
      return 1
    if y_outer:
      return 1
    if y_null:
      return 0

'''