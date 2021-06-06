
def dirReduc(arr):

  breaker = False

  while breaker is False:

    c = len(arr)
    a = 0

    while a < c-1:

      if arr[a] == "NORTH" and arr[a+1] == "SOUTH":
        arr.pop(a)
        arr.pop(a)
        
      elif arr[a] == "SOUTH" and arr[a+1] == "NORTH":
        arr.pop(a)
        arr.pop(a)
        
      elif arr[a] == "EAST" and arr[a+1] == "WEST":
        arr.pop(a)
        arr.pop(a)
        
      elif arr[a] == "WEST" and arr[a+1] == "EAST":
        arr.pop(a) 
        arr.pop(a)
        
      if a+1 >= c-2:
          breaker = True
          break
      
      c = len(arr)
      a += 1

  return arr


arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(arr))